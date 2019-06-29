/**************************************************************************
 * Zeta RF transmitter
 * This code recieves input from a joystick and sends the values 
 * Debugging lines have ben commented out, uncomment to test
 * Usage: write this onto the transmitter board and press reset
**************************************************************************/

#include <ZetaRF.h>

// Zeta modules transmit messages using fixed size packets, 
// define here the max size you want to use
#define ZETARF_PACKET_LENGTH 16
#define BUTTON_PIN 7
#define AXIS_Y A0
#define AXIS_X A1
ZetaRF zeta(10, 9, 8);  // pins: SPI CS, Shutdown, IRQ

bool transmitting = false;
uint8_t joystick[3]; // joystick array to be sent

void setup()
{
  pinMode(AXIS_Y, INPUT); // Y - axis
  pinMode(AXIS_X, INPUT); // X - axis
  pinMode(BUTTON_PIN, INPUT); // push button

  Serial.begin(115200);

  Serial.println("Starting Zeta TxRx...");

  // Initialize Zeta module, specifing channel and packet size
  zeta.begin(2, ZETARF_PACKET_LENGTH);

  Serial.println("Init done.");
}

void loop()
{
  // map joystick values to a 8 bit number, can not send bigger
  joystick[0] = map(analogRead(A0), 0, 1023, 0, 255);
  joystick[1] = map(analogRead(A1), 0, 1023, 0, 255);
  joystick[2] = digitalRead(BUTTON_PIN);

  // print sent values >Y,X,button<
  Serial.print("Sending >");
  Serial.print(joystick[0]);
  Serial.print(" ");
  Serial.print(joystick[1]);
  Serial.print(" ");
  Serial.print(joystick[2]);
  Serial.print("<\n");//*/

  // Send buffer
  transmitting = true;  // Only one at a time!
  zeta.sendPacket(2, joystick, ZETARF_PACKET_LENGTH);  // Use channel set with begin()
  // Module will automatically return to listening mode
  // Check if message was transmitted successfully
  if (zeta.checkTransmitted()) {
    transmitting = false;
    Serial.println("msg transmitted");
  } 
  delay(100); // how fast messages will be sent 
}
