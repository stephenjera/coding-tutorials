
#include <EEPROM.h>

#include "RTClib.h"

#define MINUTE 60         // 1 min (number of seconds!)
#define HOUR   (60*60)    // 1 hr
#define DAY    (60*60*24) // 1 day

//#define TIME_ALLOWED_BETWEEN_PILLS_SECS  DAY // time in seconds
//#define TIME_ALLOWED_BETWEEN_PILLS_SECS  2*MINUTE // time in seconds
#define TIME_ALLOWED_BETWEEN_PILLS_SECS  3 // time in seconds

#define MAX_NUM_OF_PILLS  30

DateTime now;
RTC_DS3231 rtc;
const int buttonPin = 2;
const int ledPin = 13; // on-board LED

// the current address in the EEPROM (i.e. which byte we're going to write to next)
int address = 0;

uint8_t numOfPills;
//uint32_t unixTimeSecs;

const int ledPins[] = {8, 9, 10, 11, 12};




void setup() {
  // initialize serial and wait for port to open:
//  Serial.begin(9600);
//  while (!Serial) {
//    ; // wait for serial port to connect. Needed for native USB port only
//  }

  //unixTimeSecs = 1580306259UL; // `158030625` & `158030625UL` used for testing


  // initialize the LED pin as an output & pushbutton pin as an input:
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);

  // Check for real-time clock module
  if (!rtc.begin())
  {
    Serial.println("Couldn't find RTC Module");
    while (1);
  }

//  // Re-initialize number of pills so don't start from what was stored in memory
//  numOfPills = MAX_NUM_OF_PILLS;

  // Get number of pills from saved memory
  numOfPills = EEPROM.read(address+4); // number of pills was stored in 5th(i.e. position 4) byte (Expected from previous sketch)
}

// ========================= ========================= ~ ALGORITHM IN PUEDOCODE ~ ========================= ========================= 
//-- Only need to do stuff when the button is pressed, otherwise remain dormant
//if(button is being pressed):
//  check last time pill was dispensed (from memory) -- reading doesn't deteriorate e2prom
//  get current time from real-time clock module (powered by battery)
//  
//  if(difference btw the times is >= 24hrs): -- Note time to be converted from secs to day
//    record/save current time in memory as time of last pill
//    dispense pill
//  else:
//    print 'It's not time yet!'
//

void loop() {
  if(digitalRead(buttonPin)) {
//    digitalWrite(ledPin, HIGH); // turn LED on
//    Serial.println("Button pressed!");

    now = rtc.now(); // just so I don't use it directly. Realy just excuse to make DateTime variable from RTC class
    uint32_t timeSinceLastPillSecs = now.unixtime() - readUnixTimeSecsFromEEPROM();
    if(timeSinceLastPillSecs >= TIME_ALLOWED_BETWEEN_PILLS_SECS) {
      saveUnixTimeSecsToEEPROM(now.unixtime()); // maybe slightly off if took a sec to get to this instruction(doubtful). However, this is time pill is dispensed tbh.
      dispensePill();
      Serial.println("Pills left: " + (String)numOfPills);
    }else {
      Serial.println("It's not time yet! ");
      
      uint32_t hrs = timeSinceLastPillSecs / (60*60);               // integer (truncated) division. uint32_t cause could be a lot of hrs since not put in days, etc.
      int mins = (timeSinceLastPillSecs - hrs*HOUR) / 60;           // ditto
      int secs = (timeSinceLastPillSecs - (hrs*HOUR + mins*MINUTE));// u get the idea
      Serial.print("Last pill was just: ");
      if(hrs > 0) Serial.print((String)hrs + " hrs  ");//Serial.printf("%d hrs  ", hrs); // printf not working on Arduino Serial
      if(mins > 0) Serial.print((String)mins + " mins  ");//Serial.printf("%d mins  ", mins);
      Serial.println((String)secs + " secs ago");//Serial.printf("%d secs\n", secs);
    }
  }


  // Display lights
  // E.g. using 5 LEDs
  // 5 means  proportion of pills left > 80%
  // 4 means  proportion of pills left > 60%
  // 3 means  proportion of pills left > 40%
  // 2 means  proportion of pills left > 20%
  // 1 means  proportion of pills left > 0%

  float proportion = numOfPills / (float)MAX_NUM_OF_PILLS;
  
  for(int i=0; i<5; i++) {
    if(proportion > i*0.2) { // for 5 LEDs setup checks 0, 0.2, 0.4, 0.6, 0.8 proportions
      digitalWrite(ledPins[i], HIGH); // turn LED on
    }else {
      digitalWrite(ledPins[i], LOW); // turn LED off
    }
  }
  

  
  delay(200); // make poll rate approx 5Hz (every 5th of a sec - 200ms)
}
// think now.unixtime() on it's own doesn't changed since stored value of DateTime var; only rtc's `now` is auto-updated






// ========================= ========================= ~ User-defined Functions ~ ========================= ========================= 
void dispensePill() {
  numOfPills--;

  EEPROM.write(address+4, numOfPills); // write the number of pills left in the 5th(i.e. position 4) byte
}


void saveUnixTimeSecsToEEPROM(uint32_t seconds) {
  // Principle: value[i] = seconds >> (8*i)
  
  for(int i=0; i<=3; i++)
    EEPROM.write(address+i, seconds >> (8*i)); // write() implicitly takes byte i.e. last 8 bits
}


uint32_t readUnixTimeSecsFromEEPROM() {
//  byte value[3];
//  for(int i=0; i<=3; i++) {
//    value[i] = EEPROM.read(address+i); // read a byte from the current address of the EEPROM
//  }
//  
//  uint32_t seconds = 0; // reading into it now, so ok to set to 0
//  for(int i=0; i<=3; i++) {
//    seconds += ((unsigned long)(value[i]) << (8*i));
//  }

  uint32_t seconds = 0; // reading into it now, so ok to set to 0
  for(int i=0; i<=3; i++)
    seconds += ((unsigned long)(EEPROM.read(address+i)) << (8*i));

  return seconds;
}
