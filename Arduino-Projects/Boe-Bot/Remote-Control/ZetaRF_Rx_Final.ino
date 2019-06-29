/*************************************************************************
* Zeta receiver code get values from the transmitter and uses tehm 
* To drive two servo motors and send an on or off signal when the butten 
* is pressed
* Debugging lines have ben commented out, uncomment to test
* Usage: write this onto the receiver board and press reset 
* WARNING: changing or adding the delay() function will cause the 
* button to behave unpredictibly
*************************************************************************/

#include <ZetaRF.h>
#include <ServoTimer2.h>

/*****************************************************************************
 * These values are defined in servotimer2 and placed here for refference
 * MIN_PULSE_WIDTH       544     // the shortest pulse sent to a servo
 * MAX_PULSE_WIDTH      2400     // the longest pulse sent to a servo
 * DEFAULT_PULSE_WIDTH  1500     // default pulse width when servo is attached
 * REFRESH_INTERVAL    20000     // minumim time to refresh servos in microseconds
*****************************************************************************/

// Zeta modules transmit messages using fixed size packets, 
// define here the max size you want to use
#define ZETARF_PACKET_LENGTH 16
#define LEFT_SERVO  6 // define the pins for the servos
#define RIGHT_SERVO 5
#define LED_PIN 2 
#define DEADZONE 40      // joystick deadzone
#define NEUTRAL_POS 128  // value when joystick is not moving

ServoTimer2 servoLeft;   // declare variables for servos
ServoTimer2 servoRight;

ZetaRF zeta(10, 9, 8);  // Pins: SPI CS, Shutdown, IRQ

int buttonState = 0; // current state of the button
unsigned long startPressed = 0;    // the time button was pressed
unsigned long endPressed = 0;      // the time button was released
unsigned long timeReleased = 0;    // the time button is released
int buttonPushCounter = 0; // counter for the number of button presses  
int newButtonState = 0;
int oldButtonState = 0;
unsigned long timeHold = 0;        // the time button is hold

void setup()
{
  servoLeft.attach(LEFT_SERVO);  // attach a pin to the servos and they will start pulsing
  servoRight.attach(RIGHT_SERVO);
  pinMode(LED_PIN, OUTPUT);

  Serial.begin(115200);
  
  Serial.println("Starting Zeta TxRx...");

  // Initialize Zeta module, specifing channel and packet size
  zeta.begin(2, ZETARF_PACKET_LENGTH);

  zeta.startListening(); // Set module in receive mode

  Serial.println("Init done.");
}

void loop()
{
  // Check incoming messages and print
  if (zeta.checkReceived())
  {
    uint8_t buf[ZETARF_PACKET_LENGTH]; // holds received message

    zeta.readPacket(buf);
    int recievedY = buf[0]; // Y value from joystick
    int recievedX = buf[1]; // X value from joystick
    int recievedBt = buf[2]; // button value from joystick
    /*Serial.print("Buffer: ");
    Serial.print(recievedY);
    Serial.print(" ");
    Serial.print(recievedX);
    Serial.print(" ");
    Serial.println(recievedButton);//*/

    newButtonState = recievedBt;
    /*Serial.print("newButtonState:");
    Serial.println(newButtonState);//*/

    if (recievedY < NEUTRAL_POS - DEADZONE)
    {
      /*//go forward
      Serial.print("go forward\n ");//*/
      servoLeft.write(MAX_PULSE_WIDTH);
      servoRight.write(MIN_PULSE_WIDTH);
    }
    else if (recievedY > NEUTRAL_POS + DEADZONE)
    {
      /*// go back
      Serial.print("go back\n ");//*/
      servoLeft.write(MIN_PULSE_WIDTH);
      servoRight.write(MAX_PULSE_WIDTH);
    }
    else if (recievedX < NEUTRAL_POS - DEADZONE)
    {
      /*// go right  
      Serial.print("go right\n ");//*/
      servoLeft.write(MAX_PULSE_WIDTH);
      servoRight.write(MAX_PULSE_WIDTH);
    }
    else if (recievedX > NEUTRAL_POS + DEADZONE)
    {
      /*//go left
      Serial.print("go left\n ");//*/
      servoLeft.write(MIN_PULSE_WIDTH);
      servoRight.write(MIN_PULSE_WIDTH);
    }
    else
    {
      /*// stop
      Serial.print("stop\n ");//*/
      servoLeft.write(DEFAULT_PULSE_WIDTH);
      servoRight.write(DEFAULT_PULSE_WIDTH);
    }

    pressButton(recievedBt); // check if button has been pressed

  }
  delay(60);
}

//function to check if button has been pressed
void pressButton(unsigned int input) {

  // button state changed
  if (newButtonState != oldButtonState)
  {
    if (buttonState == LOW) {
      startPressed = millis();
      timeReleased = startPressed - endPressed;

      if (timeReleased >= 1000) {
        buttonPushCounter++;
        /*Serial.println("Button pressed!!\n\n");
        Serial.print("number of button pushes: ");
        Serial.println(buttonPushCounter);//*/
      }
    }
  }
  oldButtonState = newButtonState;
  if (buttonPushCounter % 4 == 0) {
    digitalWrite(LED_PIN, HIGH);
  }
  else {
    digitalWrite(LED_PIN, LOW);
  }
}
