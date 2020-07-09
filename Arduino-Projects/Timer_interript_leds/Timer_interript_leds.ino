// Led code to drive leds
/* Bit shifting
 * Bitwise operators 
 * Changing on timer interrupt
 */

const int ledPin = 13;
int ledArray[] = {2,3,4,5};
volatile byte state = LOW;
 
void setup() {
   pinMode(ledPin, OUTPUT);
   // Initalise ledArray as outputs
   // int = 4 bytes thus divide by 4
   for (int i = 0; i < sizeof(ledArray)/4; i++) {
    pinMode(ledArray[i], OUTPUT);
  } 
   //TIMSK2 = TC2 Interrupt Mask Register
   // Keep old values and set Timer/Counter2, Overflow Interrupt Enable (TOIE)
   TIMSK2 = (TIMSK2 & B11111110) | 0x01; 
   
   // TCCR2B = TC2 Control Register B
   // The three Clock Select bits select the clock source to be used by the Timer/Counter.
   // Change the clock divisor (default 64)
   TCCR2B = (TCCR2B & B11111000) | 0x07; // Clock divisor = 1024
}
 
 
void loop() {
  //  COULD ADD A FUNCTION TO REMOVE FOR LOOP REPEAT
   digitalWrite(ledPin, state);
   for (int i = 0; i < sizeof(ledArray)/4; i++) {
    digitalWrite(ledArray[i])
  } 
   for (int i = 0; i < sizeof(ledArray)/4; i++) {
    digitalWrite(ledArray[i])
  } 
   
}
 
// Interrupt service routine 
ISR(TIMER2_OVF_vect){
   state = !state; // Blink LED
}
