#include "stm32f3xx.h"  // Device header

/* Function prototypes */
void led_setup();
void delay(int a);

int main(void){
	int counter = 0x0;
	led_setup();
	
	while(1){
		// BSSR = bit set reset register
		GPIOE->BSRR =  counter << 8; // Bit set register (BSRRL) L = set low
		delay(1*1000000); // On time  // Can't get accurate time with this method
		GPIOE->BSRR =  counter << 8; 
		counter++;
	}
	
}

/* Function definitions */
void led_setup() {
	RCC->AHBENR |= RCC_AHBENR_GPIOEEN; 	// Enable clock on GPIO port E
	GPIOE->MODER |= 0x55550000; // Set mode of pins 8-15 (LEDs on circle) in port E to 'Output'
	GPIOE->OTYPER &= ~(0xff00); // Set output type for LED pins to 'Open Drain'
	GPIOE->PUPDR &= ~(0x55550000); // Set Pull up/Pull down resistor configuration for LEDs
}

void delay(int a){
	  volatile int i,j;

    for (i=0 ; i < a ; i++)
    {
        j++; // Incrementing J is what occupies time, not required for delay
    }

    return;
}
