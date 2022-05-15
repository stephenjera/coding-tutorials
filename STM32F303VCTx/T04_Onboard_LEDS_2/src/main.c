#include "stm32f3xx.h"  // Device header
#include "stm32f3xx_hal.h"  
#include "mappings.h"

/* Function prototypes */
void delay(int a);
void led_setup();


int main(void){
	led_setup();
	
	while(1){
		// BSSR = bit set reset register
		GPIOE->BSRR = LD6_ON;
		GPIOE->BSRR = LD7_ON;
        GPIOE->BSRR = LD3_ON;
        delay(100000);
        //HAL_Delay(1000);
   	    GPIOE->BSRR =LD_ALL_OFF;
		//HAL_Delay(1000);
        delay(1000000);
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

