/* 
	Pete Hubbard 2019
	Loughborough University
	WSC055 Lab 1
	V.2.0
	
	The following 'c' code presents an outline for you to adapt during the laboratory
	
	*/

#include "stm32f3xx.h"                  // Device header


void delay(int a); // prototype for delay function

int main(void)
{
	// Enable clock on GPIO port E
	RCC->AHBENR |= RCC_AHBENR_GPIOEEN;
	
	// GPIOE is a structure defined in stm32f303xc.h file
	// Define settings for each output pin using GPIOE structure
	GPIOE->MODER |= 0x55550000; // Set mode of each pin in port E (doesn't work without this)
	GPIOE->OTYPER &= ~(0x0000FF00); // Set output type for each pin required in Port E (works when set to zero?)
	GPIOE->PUPDR &= ~(0x55550000); // Set Pull up/Pull down resistor configuration for Port E (still wroks when set to zero?)
	int counter = 0x0000;
	// Main programme loop - make LED 4 (attached to pin PE.0) turn on and off	
	while (1)
  {
		//uint16_t counter = 0x0000;
		
		
		GPIOE->BSRRL =  counter << 8; // Bit set register (BSRRL) L = set low
		delay(1*1000000); // On time  // Can't get accurate time with this method
		GPIOE->BSRRH =  counter << 8; 
		counter++;
		//delay(1*1000000); // Off time
		
	}

}

// Delay function to occupy processor
void delay (int a)
{
    volatile int i,j;

    for (i=0 ; i < a ; i++)
    {
        j++; // Incrementing J is what occupies time, not required for delay
    }

    return;
}
