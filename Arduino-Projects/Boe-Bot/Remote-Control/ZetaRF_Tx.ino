/*
 * Zeta RF Getting Started Code Example.
 * Basic example on how to send messages back and forth between two modules.
 *
 * Usage: write this sample on both boards and send text over serial!
 */

#include <ZetaRF.h>

// Zeta modules transmit messages using fixed size packets, define here the max size you want to use
#define ZETARF_PACKET_LENGTH 16

ZetaRF zeta(10, 9, 8);  // Pins: SPI CS, Shutdown, IRQ

int data[ZETARF_PACKET_LENGTH] = {0};
bool transmitting = false;


void setup()
{
  pinMode(A0, INPUT); // Y - axis
  pinMode(A1, INPUT); // X - axis
  Serial.begin(115200);
  delay(1000);
  
  Serial.println("Starting Zeta TxRx...");

  // Initialize Zeta module, specifing channel and packet size
  zeta.begin(2, ZETARF_PACKET_LENGTH);
  
  // Set module in receive mode
  zeta.startListening();

  Serial.println("Init done.");
}

uint8_t joystick[3];

void loop()
{
  // Send any data received from serial
 /* if (Serial.available() && !transmitting) {
    int s = Serial.readBytes(data, ZETARF_PACKET_LENGTH);

    // Pad with zeros
    for (int i = s; i < ZETARF_PACKET_LENGTH; i++) {
      data[i] = 0;
    }*/
  joystick[0] = map(analogRead(A0), 0, 1023, 0, 255);
  joystick[1] = map(analogRead(A1), 0, 1023, 0, 255);
  joystick[2] = 100;
    int input0 = joystick[0];
    int input1 = joystick[1];
    int input2 = joystick[2];
    Serial.print("Sending >");
    Serial.print(input0);
    Serial.print(input1);
    Serial.print(input2);
    Serial.print("<\n");

    // Send buffer
    transmitting = true;  // Only one at a time!
    zeta.sendPacket(2,joystick,ZETARF_PACKET_LENGTH);  // Use channel set with begin()
    // Module will automatically return to listening mode
 // }

  // Check if message was transmitted successfully
  if (zeta.checkTransmitted()) {
    transmitting = false;
    Serial.println("msg transmitted");
  }//*/
/*
  // Check incoming messages and print
  if (zeta.checkReceived()) {
    Serial.print("> ");
    zeta.readPacket((uint8_t*)data);
    Serial.write(data, ZETARF_PACKET_LENGTH);
    Serial.print('\n');
  }//*/
  
  delay(10);
}
