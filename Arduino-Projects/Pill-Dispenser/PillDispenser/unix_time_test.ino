//
//#include <EEPROM.h>
//
//// the current address in the EEPROM (i.e. which byte we're going to write to next)
//int address = 0;
//
//uint32_t unixTimeSecs;
//
//void setup() {
//  // initialize serial and wait for port to open:
//  Serial.begin(9600);
//  while (!Serial) {
//    ; // wait for serial port to connect. Needed for native USB port only
//  }
//
//  unixTimeSecs = 1580306259UL; // `158030625` & `158030625UL` used for testing
//}
//
//void loop() {
//  // Write, wait, read the value, increment, then print via serial
//
//  // Write,
//  // wait
//  // read the value,
//  // increment,
//  // print via serial
//  
//  
//  saveUnixTimeSecsToEEPROM(unixTimeSecs);
//  delay(1000);
//  unixTimeSecs = readUnixTimeSecsFromEEPROM();
//  unixTimeSecs++;
//
//  
//  Serial.print(address);
//  Serial.print("\t");
//  Serial.print("Increment unixTimeSecs to ");
//  Serial.print(unixTimeSecs, DEC);
//  Serial.println();
//
//}
//
//
//// ========================= ========================= ~ User-defined Functions ~ ========================= ========================= 
//void saveUnixTimeSecsToEEPROM(uint32_t seconds) {
//  // Principle: value[i] = seconds >> (8*i)
//  
//  for(int i=0; i<=3; i++)
//    EEPROM.write(address+i, seconds >> (8*i)); // write() implicitly takes byte i.e. last 8 bits
//}
//
//
//uint32_t readUnixTimeSecsFromEEPROM() {
////  byte value[3];
////  for(int i=0; i<=3; i++) {
////    value[i] = EEPROM.read(address+i); // read a byte from the current address of the EEPROM
////  }
////  
////  uint32_t seconds = 0; // reading into it now, so ok to set to 0
////  for(int i=0; i<=3; i++) {
////    seconds += ((unsigned long)(value[i]) << (8*i));
////  }
//
//  uint32_t seconds = 0; // reading into it now, so ok to set to 0
//  for(int i=0; i<=3; i++)
//    seconds += ((unsigned long)(EEPROM.read(address+i)) << (8*i));
//
//  return seconds;
//}
