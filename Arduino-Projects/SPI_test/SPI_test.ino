char dataString[50] = {0};
int a =0; 
String data;
int ledPin = 2;

void setup() {
Serial.begin(9600);              //Starting serial communication
pinMode(LED_BUILTIN, OUTPUT);
pinMode(ledPin, OUTPUT);    
}
  
void loop() {
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(200);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(200);
  if (Serial.available() > 0) {
    data = Serial.read();
      if (data == "hello"){
        digitalWrite(ledPin, HIGH);   // turn the LED on (HIGH is the voltage level)
        delay(1000);                       // wait for a second
        digitalWrite(ledPin, LOW);    // turn the LED off by making the voltage LOW
        delay(1000);                      // wait for a second
        } 
        data = "baby";
//  a++;                          // a value increase every loop
//  sprintf(dataString,"%02X",a); // convert a value to hexa 
//  Serial.println(dataString);   // send the data
//  delay(1000);                  // give the loop some break
  }
}
