/*******************
 * H bridge gude 
 * 10 = rotate 
 * 01 = rotate
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
}

void loop() {
  digitalWrite(ENABLE,HIGH); // enable on
  
  digitalWrite(DIRA,HIGH); //one way
  digitalWrite(DIRB,LOW);
  /* CURRENTLY IGNORES EVERYTHING BEYOND THIS POINT??
  delay(500); // spin for 3 seconds 
  digitalWrite(ENABLE,LOW);
  digitalWrite(DIRA,HIGH); //stop
  digitalWrite(DIRB,HIGH);*/
}
