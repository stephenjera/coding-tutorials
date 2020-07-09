// Led code to drive leds
/* Bit shifting
 * Bitwise operators 
 * Changing on timer interrupt
 */

const int ledPin = 13;
volatile byte state = LOW;
 
 
void setup() {
   pinMode(ledPin, OUTPUT);
   //TIMSK2 = TC2 Interrupt Mask Register
   // Keep old values and set Timer/Counter2, Overflow Interrupt Enable (TOIE)
   TIMSK2 = (TIMSK2 & B11111110) | 0x01; 
   
   // TCCR2B = TC2 Control Register B
   // The three Clock Select bits select the clock source to be used by the Timer/Counter.
   // Change the clock divisor (default 64)
   TCCR2B = (TCCR2B & B11111000) | 0x07; // Clock divisor = 1024
}
 
 
void loop() {
   digitalWrite(ledPin, state);
}
 
// Interrupt service routine 
ISR(TIMER2_OVF_vect){
   state = !state; // Blink LED
}
