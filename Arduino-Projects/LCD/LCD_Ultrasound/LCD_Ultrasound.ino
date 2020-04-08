#include <LiquidCrystal.h>
#include "SR04.h"

// Setup ultrasound
#define TRIG_PIN 12
#define ECHO_PIN 11
SR04 sr04 = SR04(ECHO_PIN,TRIG_PIN);
long distance;

// Create an LCD object. Parameters: (RS, E, D4, D5, D6, D7):
LiquidCrystal lcd = LiquidCrystal(2, 3, 4, 5, 6, 7);
void setup() {
  // Specify the LCD's number of columns and rows. Change to (20, 4) for a 20x4 LCD:
  lcd.begin(16, 2);
  
}
void loop() {
  distance = sr04.Distance();  

  // Set the cursor on the third column and the first row, counting starts at 0:
  lcd.setCursor(2, 0);
  
  // Print the distance
  lcd.print(distance);
  lcd.print(" cm");
  
  // Refrersh display
  delay(1000);
  lcd.clear();
  
}
