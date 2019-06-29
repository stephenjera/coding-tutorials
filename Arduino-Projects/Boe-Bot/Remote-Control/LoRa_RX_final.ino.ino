// Arduino9x_RX
// -*- mode: C++ -*-
// Example sketch showing how to create a simple messaging client (receiver)
// with the RH_RF95 class. RH_RF95 class does not provide for addressing or
// reliability, so you should only use RH_RF95 if you do not need the higher
// level messaging abilities.
// It is designed to work with the other example Arduino9x_TX

#include <SPI.h>
#include <RH_RF95.h>
#include <ServoTimer2.h>  // the servo library

/*****************************************************************************
MIN_PULSE_WIDTH       544     // the shortest pulse sent to a servo
MAX_PULSE_WIDTH      2400     // the longest pulse sent to a servo
DEFAULT_PULSE_WIDTH  1500     // default pulse width when servo is attached
REFRESH_INTERVAL    20000     // minumim time to refresh servos in microseconds
*****************************************************************************/

#define RFM95_CS 10 // Chip select
#define RFM95_RST 9 // Reset
#define RFM95_INT 2 // Interrupt

// define the pins for the servos
#define LEFTPIN  5
#define RIGHTPIN 6
#define DEADZONE 20      // joystick deadzone
#define NEUTRAL_POS 128  // value when joystick is not moving
ServoTimer2 servoLeft;   // declare variables for up to eight servos
ServoTimer2 servoRight;

// Change to 434.0 or other frequency, must match RX's freq!
#define RF95_FREQ 868.0

// Singleton instance of the radio driver
RH_RF95 rf95(RFM95_CS, RFM95_INT);

void setup()
{
  pinMode(RFM95_RST, OUTPUT);
  digitalWrite(RFM95_RST, HIGH);

  servoLeft.attach(LEFTPIN);     // attach a pin to the servos and they will start pulsing
  servoRight.attach(RIGHTPIN);
  pinMode(A0, INPUT); // Joystick y_axis
  pinMode(A1, INPUT); // Joystick x_axis

  while (!Serial);
  Serial.begin(9600);
  delay(100);

  // manual reset
  digitalWrite(RFM95_RST, LOW);
  delay(10);
  digitalWrite(RFM95_RST, HIGH);
  delay(10);

  while (!rf95.init()) {
    Serial.println("LoRa radio init failed");
    while (1);
  }
  Serial.println("LoRa radio init OK!");

  // Defaults after init are 434.0MHz, modulation GFSK_Rb250Fd250, +13dbM
  if (!rf95.setFrequency(RF95_FREQ)) {
    Serial.println("setFrequency failed");
    while (1);
  }
  Serial.print("Set Freq to: "); Serial.println(RF95_FREQ);

  // Defaults after init are 434.0MHz, 13dBm, Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on

  // The default transmitter power is 13dBm, using PA_BOOST.
  // If you are using RFM95/96/97/98 modules which uses the PA_BOOST transmitter pin, then 
  // you can set transmitter powers from 5 to 23 dBm:
  rf95.setTxPower(23, false);
}

void loop()
{
  if (rf95.available())
  {
    // Should be a message for us now   
    uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
    uint8_t len = sizeof(buf);
    
    if (rf95.recv(buf, &len))
    {
      if (buf[0] < NEUTRAL_POS - DEADZONE)
      {
        // go forward
        servoLeft.write(MAX_PULSE_WIDTH);
        servoRight.write(MIN_PULSE_WIDTH);
      }
      else if (buf[0] > NEUTRAL_POS + DEADZONE)
      {
        // go back        
        servoLeft.write(MIN_PULSE_WIDTH);        
        servoRight.write(MAX_PULSE_WIDTH);
      }
      else if (buf[1] < NEUTRAL_POS - DEADZONE)
      {
        // go right      
        servoLeft.write(MAX_PULSE_WIDTH);        
        servoRight.write(MAX_PULSE_WIDTH);
      }
      else if (buf[1] > NEUTRAL_POS + DEADZONE)
      {
        //go left        
        servoLeft.write(MIN_PULSE_WIDTH);       
        servoRight.write(MIN_PULSE_WIDTH);
      }
      else {
        // stop
        servoLeft.write(DEFAULT_PULSE_WIDTH);
        servoRight.write(DEFAULT_PULSE_WIDTH);
      }     
    }
  }
}
