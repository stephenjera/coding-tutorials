// Led code to drive leds
/* Bit shifting
 * Bitwise operators 
 * Changing on timer interrupt
 */

// DDR = Data Direction Register 0 = MSB
// DDRx (e.g. DDRD for port D) is the register that controls if pins are input or output. (0=input, 1=output)


uint8_t leds = 0x01;
 
void setup() {
   // Set port D as outputs
   DDRD = 0xFF;
   
   // TIMSK2 = TC2 Interrupt Mask Register
   // Keep old values and set Timer/Counter2, Overflow Interrupt Enable (TOIE)
   TIMSK2 = (TIMSK2 & B11111110) | 0x01; 
   
   // TCCR2B = TC2 Control Register B
   // The three Clock Select bits select the clock source to be used by the Timer/Counter.
   // Change the clock divisor (default 64)
   TCCR2B = (TCCR2B & B11111000) | 0x07; // Clock divisor = 1024
}
 
 
void loop() {
  // PORTx (e.g. PORTD for port D) reads or write the bits.
  PORTD = leds; // Turn LEDs on or off
  if(leds == 0x00){
    delay(500);
    leds = 0x01;
  }
}
 
// Interrupt service routine 
ISR(TIMER2_OVF_vect){
 leds = leds << 1;
}
