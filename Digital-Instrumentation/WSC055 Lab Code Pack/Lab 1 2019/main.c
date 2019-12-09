/* 
	Pete Hubbard 2019
	Loughborough University
	WSC055 Lab 1
	V.2.0
	
	The following 'c' code presents an outline for you to adapt during the laboratory
	
	*/

#include "stm32f3xx.h"                  // Device header

int counter = 0x0000; // Global variable

// Function prototypes
void delay(int a); // Prototype for delay function
void setDAC(void); // Prototype for DAC
void setADC(void); // Prototype for ADC

int main(void)
{
	/* Setting up timer*/
	RCC->APB1ENR |= RCC_APB1ENR_TIM3EN; // Directs clock pules to timer
	TIM3->PSC = 7999; // prescalor value in Timer ‘x’ as 100
	TIM3->ARR = 999; // Auto-Reset Register of Timer ‘x’ set to 1000 counts
	TIM3->CR1 |= TIM_CR1_CEN; // //Set Timer Control Register to start timer
	TIM3->DIER |= TIM_DIER_UIE; // Set DIER register to watch out for an ‘Update’ Interrupt Enable (UIE) – or 0x00000001
	
	RCC->AHBENR |= RCC_AHBENR_GPIOEEN; // Enable clock on GPIO port E
	
	NVIC_EnableIRQ(TIM3_IRQn);  //  Enable Timer ‘3’ interrupt request in NVIC
	
	// GPIOE is a structure defined in stm32f303xc.h file
	// Define settings for each output pin using GPIOE structure
	GPIOE->MODER |= 0x55550000; // Set mode of each pin in port E (doesn't work without this)
	GPIOE->OTYPER &= ~(0x0000FF00); // Set output type for each pin required in Port E (works when set to zero?)
	GPIOE->PUPDR &= ~(0x55550000); // Set Pull up/Pull down resistor configuration for Port E (still wroks when set to zero?)
	setDAC();
	setADC();
	
	// Main programme loop 
	while (1){}

};

// Interrupt handler
void TIM3_IRQHandler()
{
	void delay(int a); // prototype for delay function
	if ((TIM3->SR & TIM_SR_UIF) !=0) // Check interrupt source is from the ‘Update’ interrupt flag
	{
		//...INTERRUPT ACTION HERE
		
		//delay(1*1000000); // On time  // Can't get accurate time with this method
		GPIOE->BSRRH =  counter << 8; 
		counter++;
		GPIOE->BSRRL =  counter << 8; // Bit set register (BSRRL) L = set low
	}
	TIM3->SR &= ~TIM_SR_UIF; // Reset ‘Update’ interrupt flag in the SR register
	
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

void setDAC(void){
	RCC->APB1ENR |= RCC_APB1ENR_DAC1EN; // Connect DAC to system clock
	DAC1->CR |= DAC_CR_BOFF1; // Disable the ‘buffer’ function in the DAC control register
	DAC1->CR |= DAC_CR_EN1; // Enable DAC peripheral
	//DAC1_DHR8R1
}

void setADC(void){
	/*startup procedure*/
	ADC1->CR &= ~ADC_CR_ADVREGEN; // Reset voltage regulator
	ADC1->CR |= ADC_CR_ADVREGEN_0; // 01: ADC Voltage regulator enabled
	delay(50); // Wait for calibration to be done
	
	/*Calibrate ADC*/
	ADC1->CR &= ~ADC_CR_ADCALDIF; // calibration in Single-ended inputs Mode.
	ADC1->CR |= ADC_CR_ADCAL; // Start ADC calibration
	while (ADC1->CR & ADC_CR_ADCAL); // wait until calibration done
 // calibration_value = ADC1->CALFACT; // Get Calibration Value ADC1
	
	//Enable Clock 
	RCC->CFGR2 |= RCC_CFGR2_ADCPRE12_DIV2;
	RCC->AHBENR |= RCC_AHBENR_ADC12EN; // Clock for ADC 1 and 2
	ADC1_2_COMMON->CCR |= 0x00010000;
}
