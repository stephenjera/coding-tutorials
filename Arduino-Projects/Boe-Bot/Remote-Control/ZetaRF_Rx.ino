/*
 * Zeta RF Getting Started Code Example.
 * Basic example on how to send messages back and forth between two modules.
 *
 * Usage: write this sample on both boards and send text over serial!
 */

#include <ZetaRF.h>
#include <ServoTimer2.h>
/*****************************************************************************
MIN_PULSE_WIDTH       544     // the shortest pulse sent to a servo
MAX_PULSE_WIDTH      2400     // the longest pulse sent to a servo
DEFAULT_PULSE_WIDTH  1500     // default pulse width when servo is attached
REFRESH_INTERVAL    20000     // minumim time to refresh servos in microseconds
*****************************************************************************/

// Zeta modules transmit messages using fixed size packets, define here the max size you want to use
#define ZETARF_PACKET_LENGTH 16

// define the pins for the servos
#define LEFTPIN  5
#define RIGHTPIN 6

#define DEADZONE 20      // joystick deadzone
#define NEUTRAL_POS 128  // value when joystick is not moving

ServoTimer2 servoLeft;   // declare variables for up to eight servos
ServoTimer2 servoRight;

ZetaRF zeta(10, 9, 8);  // Pins: SPI CS, Shutdown, IRQ

bool transmitting = false;

void setup()
{
  Serial.begin(115200);
  delay(1000);
  servoLeft.attach(LEFTPIN);     // attach a pin to the servos and they will start pulsing
  servoRight.attach(RIGHTPIN);
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
    uint8_t buf[ZETARF_PACKET_LENGTH];
    
    Serial.print("> ");
    zeta.readPacket(buf);
    Serial.println(buf[0]);
    Serial.println(buf[1]);
    Serial.println(buf[2]);

    if (buf[0] < NEUTRAL_POS - DEADZONE)
      {
        // go forward
        Serial.print("go forward ");
        servoLeft.write(MAX_PULSE_WIDTH);
        servoRight.write(MIN_PULSE_WIDTH);
      }
      else if (buf[0] > NEUTRAL_POS + DEADZONE)
      {
        // go back
        Serial.print("go back ");        
        servoLeft.write(MIN_PULSE_WIDTH);        
        servoRight.write(MAX_PULSE_WIDTH);
      }
      else if (buf[1] < NEUTRAL_POS - DEADZONE)
      {
        // go right  
        Serial.print("go right ");    
        servoLeft.write(MAX_PULSE_WIDTH);        
        servoRight.write(MAX_PULSE_WIDTH);
      }
      else if (buf[1] > NEUTRAL_POS + DEADZONE)
      {
        //go left
        Serial.print("go left ");        
        servoLeft.write(MIN_PULSE_WIDTH);       
        servoRight.write(MIN_PULSE_WIDTH);
      }
      else 
      {
        // stop
        Serial.print("stop "); 
        servoLeft.write(DEFAULT_PULSE_WIDTH);
        servoRight.write(DEFAULT_PULSE_WIDTH);
      }
           
  }
  
  delay(10);
}
