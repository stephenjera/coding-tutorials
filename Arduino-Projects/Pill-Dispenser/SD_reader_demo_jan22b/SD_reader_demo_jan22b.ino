/*
  SD card read/write
 
 This example shows how to read and write data to and from an SD card file   
 The circuit:
 * SD card attached to SPI bus as follows:
 ** MOSI - pin 11
 ** MISO - pin 12
 ** CLK - pin 13
 ** CS - pin 4
 
 created   Nov 2010
 by David A. Mellis
 modified 9 Apr 2012
 by Tom Igoe
 
 This example code is in the public domain.
   
 */
 
#include <SPI.h>
#include <SD.h>

File myFile;
int num = 0;

void setup()
{
 // Open serial communications and wait for port to open:
  Serial.begin(9600);
   while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }


  Serial.print("Initializing SD card...");
  // On the Ethernet Shield, CS is pin 4. It's set as an output by default.
  // Note that even if it's not used as the CS pin, the hardware SS pin 
  // (10 on most Arduino boards, 53 on the Mega) must be left as an output 
  // or the SD library functions will not work. 
   pinMode(10, OUTPUT);
   
  if (!SD.begin(10)) {
    Serial.println("initialization failed!");
    return;
  }
  Serial.println("initialization done.");


  
  // open the file. note that only one file can be open at a time,
  // so you have to close this one before opening another.
  myFile = SD.open("test.txt", FILE_WRITE);
  
  // if the file opened okay, write to it:
  if (myFile) {
    Serial.print("Writing to test.txt...");
    myFile.println("30");
    myFile.close(); // close the file:
    Serial.println("done.");
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening test.txt");
  }

  
  
  // re-open the file for reading:
  myFile = SD.open("test.txt");
  if (myFile) {
    Serial.println("test.txt:");
    
    // read from the file until there's nothing else in it:
    while (myFile.available()) {
      Serial.write(myFile.read());
      //char character = myFile.read();
      //if((character >='0') && (character <='9'))
        //Serial.write(character - '0');
        //Serial.print(character - '0');
        

//      if(character == '\n')
  //      Serial.println();
      
    }
    // close the file:
    myFile.close();
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening test.txt");
  }
  //num = 30;
  //writeToDatabase((num)+"");
  
}


void loop()
{
//  // nothing happens after setup

  
  //if(num > 0) {
//    writeToDatabase((num)+""); // writes num as a String
//    num = readFromDatabase().toInt();
//    Serial.println(num);
//    num--;
//    delay(1000);
  //}
}


//char const* readFromDatabase() {
String readFromDatabase() {
  String str = "";
  
  // open the file for reading:
  myFile = SD.open("test.txt");
  if (myFile) {
    Serial.println("Read from file...");
    
    // read from the file until there's nothing else in it:
    while (myFile.available()) {
      //Serial.write(myFile.read());
      char character = myFile.read();
//      if((character >='0') && (character <='9'))
//        //Serial.write(character - '0');
//        Serial.print(character - '0');
//      if(character == '\n')
//        Serial.println();
      str += character;
    }
    // close the file:
    myFile.close();
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening file");
  }

  Serial.println("done reading");
  ////return (const char*)str;
  //return str.c_str();
  return str;
}

void writeToDatabase(char const* msg) {
  // OVERwrite to a file the lazy way by deleting it first
  SD.remove("test.txt");
  myFile = SD.open("test.txt", FILE_WRITE);
  
  // if the file opened okay, write to it:
  if (myFile) {
    Serial.println("Writing to file...");
    myFile.println(msg);
    myFile.close(); // close the file:
    Serial.println("done.");
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening file");
  }
}
