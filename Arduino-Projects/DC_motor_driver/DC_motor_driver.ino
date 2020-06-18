/*******************
 * H bridge gude 
 * 10 = left 
 * 01 = right
 * 00 or 11 = stop 
 *******************/

#define ENABLE 5
// Used to control the H bridge 
#define DIRA 6 
#define DIRB 7

void setup() {
  pinMode(ENABLE,OUTPUT);
  pinMode(DIRA, OUTPUT);
  pinMode(DIRB, OUTPUT);
  Serial.begin(9600);
  digitalWrite(ENABLE,HIGH); // enable on, 
}

void loop() {
  
  digitalWrite(DIRA,HIGH); //one way
  digitalWrite(DIRB,LOW);
  delay(3000); // spin for 3 seconds 
  //digitalWrite(ENABLE,LOW);
  digitalWrite(DIRA,HIGH); //stop
  digitalWrite(DIRB,HIGH);
  delay(3000); // off for 3 seconds 
  digitalWrite(DIRA,LOW); //other way
  digitalWrite(DIRB,HIGH);
  delay(3000); // spin for 3 seconds 
}
