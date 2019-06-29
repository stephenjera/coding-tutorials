// LoRa 9x_TX
// -*- mode: C++ -*-
// Example sketch showing how to create a simple messaging client (transmitter)
// with the RH_RF95 class. RH_RF95 class does not provide for addressing or
// reliability, so you should only use RH_RF95 if you do not need the higher
// level messaging abilities.
// It is designed to work with the other example LoRa9x_RX

#include <SPI.h>
#include <RH_RF95.h>

#define RFM95_CS 10 // Chip select
#define RFM95_RST 9 // Reset
#define RFM95_INT 2 // Interrupt

// Change to 434.0 or other frequency, must match RX's freq!
#define RF95_FREQ 868.0

// Singleton instance of the radio driver
RH_RF95 rf95(RFM95_CS, RFM95_INT);

void setup()
{
  pinMode(RFM95_RST, OUTPUT);
  digitalWrite(RFM95_RST, HIGH);
  pinMode(A0, INPUT); // Y - axis
  pinMode(A1, INPUT); // X - axis

  while (!Serial); // pause unitl serial monitor opens
  Serial.begin(9600);
  delay(100);
  
  Serial.println("Arduino LoRa TX Test!");
  
  // manual reset
  digitalWrite(RFM95_RST, LOW);
  delay(10);
  digitalWrite(RFM95_RST, HIGH);
  delay(10);
  //NO IDEA WHY THIS WHILE LOOP IS NEEDED?? DOESN'T WORK WITHOUT IT THOUGH
  while (!rf95.init())
  {
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
  
  //Defaults after init are 434.0MHz, 13dBm, Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on

  // The default transmitter power is 13dBm, using PA_BOOST.
  // If you are using RFM95/96/97/98 modules which uses the PA_BOOST transmitter pin, then 
  // you can set transmitter powers from 5 to 23 dBm:
  rf95.setTxPower(23, false);
}

uint8_t joystick[3];

void loop()
{
  joystick[0] = map(analogRead(A0), 0, 1023, 0, 255);
  joystick[1] = map(analogRead(A1), 0, 1023, 0, 255);
  joystick[3] = 100;
   
  rf95.send(joystick, sizeof(joystick));
  rf95.waitPacketSent();

  delay(60);
}
