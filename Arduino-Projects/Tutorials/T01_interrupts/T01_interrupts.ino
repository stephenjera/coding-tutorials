// pin definitions
int buttonPin = 2; // interrupt capable pin

volatile int buttonFlag; // value can change without Arduino knowing

void setup() {
  // setup pin modes
  pinMode(buttonPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(buttonPin), ISR_button, CHANGE);

}

void loop() {
  // put your main code here, to run repeatedly:
  buttonFlag = 0;
}

void ISR_button(){
    buttonFlag = 1;
  }
