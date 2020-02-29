/*Code for Liquid Level Sensor Circuit Built with an Arduino*/

const int sensorPin = 0; // Sensor pin connected to analog pin A0
int liquid_level;

void setup() { 
  Serial.begin(9600); // Sets the baud rate for data transfer in bits/second 
  pinMode(sensorPin, INPUT);// The liquid level sensor will be an input to the arduino 
}

void loop() { 
  liquid_level = analogRead(sensorPin); // Arduino reads the value from the liquid level sensor 
  Serial.println(liquid_level);// Prints out liquid level sensor reading 
  delay(1000);//delays 100ms
}
