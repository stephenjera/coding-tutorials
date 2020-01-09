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
float read_ADC(void);

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
	read_ADC();
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
		//GPIOE->BSRRH =  counter << 8; 
		//counter++;
		//GPIOE->BSRRL =  counter << 8; // Bit set register (BSRRL) L = set low
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
	
	/*== Enable ADC Clock ==*/
	// Divide CPU clock for ADC
	RCC->CFGR2 |= RCC_CFGR2_ADCPRE12_DIV2; // May need DIV6 instead
	RCC->AHBENR |= RCC_AHBENR_ADC12EN; // Clock for ADC 1 and 2
	ADC1_2_COMMON->CCR |= 0x00010000; // WHAT IS THIS DOING?
	
	/*== Setup Voltage Regulator ==*/
	// MUST BE SET THEN RESET?
	ADC1->CR &= ~ADC_CR_ADVREGEN; // Reset voltage regulator
	ADC1->CR |= ADC_CR_ADVREGEN_0; // 01: ADC Voltage regulator enabled
	delay(10); // Wait for calibration to be done
	
	/*==Calibrate ADC==*/
	ADC1->CR &= ~ADC_CR_ADCALDIF; // calibration in Single-ended inputs Mode.
	ADC1->CR |= ADC_CR_ADCAL; // Start ADC calibration
	while(ADC1->CR & ADC_CR_ADCAL); // wait until calibration done (bitwise and until 0 is returned)
	// while (ADC1->CR & ~ADC_CR_ADCAL) != 0); // Alt calibration test
  // calibration_value = ADC1->CALFACT; // Get Calibration Value ADC1
	
	/*== Configure GPIO ==*/
	RCC->AHBENR |= RCC_AHBENR_GPIOAEN;
	GPIOA->MODER |= 0x00000002; // Set mode of pin PA0 to '10' for 'Analogue'
	
	/*== Configure ADC ==*/
	ADC1->CFGR &= ~ADC_CFGR_CONT; // ADC_ContinuousConvMode_Enable
	ADC1->CFGR |= ADC_CFGR_RES_1; // 8-bit data resolution  = 0x00000010
	ADC1->CFGR &= ~ADC_CFGR_RES_0; // CHECK WHAT THIS IS DOING  = 0x00000008  setting register to 0?
	ADC1->CFGR &= ~ADC_CFGR_ALIGN; // Right data alignment

	/*== Configure Multiplexing ==*/ 
	//ADC1->SQR1 |= ADC_SQR1_SQ1_2 | ADC_SQR1_SQ1_1 | ADC_SQR1_SQ1_0; // SQ1 = 0x07, start converting ch7
	ADC1->SQR1 |= ADC_SQR1_SQ1_0; // SQ1 = 0x01, start converting ch1 FIND OUT MORE
  ADC1->SQR1 &= ~ADC_SQR1_L; // ADC regular channel sequence length = 0 => 1 conversion/sequence
	ADC1->SMPR1 |= ADC_SMPR1_SMP7_1 | ADC_SMPR1_SMP7_0; // = 0x03 => sampling time 7.5 ADC clock cycles
	
	/*== Enable ADC ==*/
	ADC1->CR |= ADC_CR_ADEN; // Enable ADC1
	while(!ADC1->ISR & ADC_ISR_ADRD); // wait for ADRDY (not ISR = 0 therfore true until ardy = 1)
	//ADC1->CR |= ADC_CR_ADSTART; // Start ADC1 Software Conversion
	
	/*== Wait for EOC ==*/
/*	int logictest =1;
	while(logictest){
		logictest = !(ADC1->ISR & ADC_ISR_EOC);
	} // Test EOC flag (and with 0 EOC reg will always give 1)
	//while(!(ADC1->ISR & ADC_ISR_EOC));
  // While loop throws an error without the space
	int ADC1ValueNew = ADC1->DR; // Get ADC1 converted data*/
}

float read_ADC() {
	// 1. Start the conversion by setting the ADSTART bit high
	ADC1->CR |= ADC_CR_ADSTART; // Start ADC1 Software Conversion
	
	// 2. Wait for the end of conversion (reported in the ADCx_ISR register by the EOC bit going high)
  // 3. Read data from the data register (ADCx_DR). Doing this resets the EOC flag.
	while(!(ADC1->ISR & ADC_ISR_EOC)){} // Test EOC flag
  int ADC1ConvertedValue = ADC1->DR; // Get ADC1 converted data, returned as 8bit value(or whatever set resolution)
  // int ADC1ConvertedVoltage = (ADC1ConvertedValue *3300)/4096; // Compute the voltage, for 12bit, in mV
	float ADC1ConvertedVoltage = (ADC1ConvertedValue *3.3)/(float)256; // Compute the voltage, for 8bit, in V
	return ADC1ConvertedVoltage;
}

/*==== ADC set up ====*/
// http://homepage.cem.itesm.mx/carbajal/Microcontrollers/SLIDES/STM32F3%20ADC.pdf
// https://community.st.com/s/question/0D50X00009XkgZz/stm32f3-adc-in-differential-mode
// https://www.youtube.com/watch?v=qqGsy06mris&t=466s
