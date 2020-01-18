/* 
	Pete Hubbard 2019
	Loughborough University
	WSC055 Lab 1
	V.2.0
	
	The following 'c' code presents an outline for you to adapt during the laboratory
	
	*/

#include "stm32f3xx.h"                  // Device header

int counter = 0x0000; // Global variable

uint32_t ADC1ConvertedValue = 0;
uint16_t ADC1ConvertedVoltage = 0;
uint16_t calibration_value = 0;
volatile uint32_t TimingDelay = 0;

// Function prototypes

void Delay (uint32_t nTime);
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
	//read_ADC();
	
	// Main programme loop 
	while (1){
	
		ADC1ConvertedValue = ADC1->DR;
	
	}

};

// Interrupt handler
void TIM3_IRQHandler()
{
	void delay(int a); // prototype for delay function
	if ((TIM3->SR & TIM_SR_UIF) !=0) // Check interrupt source is from the ‘Update’ interrupt flag
	{
		//...INTERRUPT ACTION HERE
//		DAC1->DHR8R1 = counter ; // Holding Register for Right aligned, 8-bit data
//		//counter++;
//		//delay(1*1000000); // On time  // Can't get accurate time with this method
//		GPIOE->BSRRH =  counter << 8; 
//		counter++;
//		GPIOE->BSRRL =  counter << 8; // Bit set register (BSRRL) L = set low
//		DAC1->DHR8R1 = counter ; // Holding Register for Right aligned, 8-bit data
		//ADC1ConvertedValue = ADC1->DR;
		
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
}

void setADC(void){
		uint8_t initc = 0;
	//Enable Clock Connection
	RCC->CFGR2			|=	RCC_CFGR2_ADCPRE12_DIV2;
	RCC->AHBENR			|=	RCC_AHBENR_ADC12EN;
	ADC1_2_COMMON->CCR	|=	ADC12_CCR_CKMODE_0;	//Synchronous clock mode HCLK/1  0x00010000;

	//TIM3->CR1	|=	TIM_CR1_CEN; // Enabled in timers

	//Enable VReg
	ADC1->CR	&=	~ADC_CR_ADVREGEN;	//Reset
	ADC1->CR	|=	 ADC_CR_ADVREGEN_0;	//Enable

	while(100 > initc)
		initc++;

	/////////
	//Calibrate
	ADC1->CR	&=	~ADC_CR_ADCALDIF;
	ADC1->CR	|=	 ADC_CR_ADCAL;
	while (ADC1->CR & ADC_CR_ADCAL); // Wait until calibrated
	//calibration_value	 =	ADC1->CALFACT;		// Get Calibration Value ADC1
	/*------------------------------------------
	// Set input pin
	// PA0 ADC1_IN1 .. PA3 IN4, PF4 IN5
	// PC0 ADC12_IN6 .. PC3 IN9, PF2 IN10
	// Enable GPIOA for connecting timer to PA0 
	//------------------------------------------*/
	RCC->AHBENR		|=	RCC_AHBENR_GPIOAEN;
	GPIOA->MODER	|=	3;//0x0000C000;

	//--
	//Config using ADC1_CFGR
	ADC1->CFGR	|=	 ADC_CFGR_RES_1;	//Set to 8bit
	ADC1->CFGR	&=	~ADC_CFGR_ALIGN;	//right align
	ADC1->CFGR	&=	~ADC_CFGR_CONT;		//notcontinuous

	//ADC1->CR |= ADC_CR_ADEN;
	//Multiplex Options
	// ADC1->SQR1 |= ADC_SQR1_SQ1_2 | ADC_SQR1_SQ1_1 | ADC_SQR1_SQ1_0; // SQ1 = 0x07, start converting ch7
	//ADC1->SQR1	&=	~ADC_SQR1_SQ1;		// SQ1 = 0x07, start converting ch7
	ADC1->SQR1	|= 	 ADC_SQR1_SQ1_0;
	ADC1->SQR1	&=	~ADC_SQR1_L;		// ADC regular channel sequence length = 0 => 1 conversion/sequence
	//ADC1->SMPR1	|=	 ADC_SMPR1_SMP7_2 | ADC1_SMPR1_SMP7_1 | ADC_SMPR1_SMP7_0; // 101 => 74 ADC clock cycles ~= 1us
	ADC1->SMPR1 |= ADC_SMPR1_SMP0;

	ADC1->CR		|=	 ADC_CR_ADEN;		// Enable ADC1
	//while(!ADC1->ISR & ADC_ISR_ADRD);	// wait for ADRDY

	//ADC1->SQ &= sqr1!0x0F;

	ADC1->IER 	|= 	 ADC_IER_EOC;
	//ADC1->IER		|=	 ADC_IER_RDY;
	NVIC_EnableIRQ(ADC1_2_IRQn); // Enable Interrupt

	/////////
	return;

}

void Delay (uint32_t nTime)
{
 TimingDelay = nTime;
 while (TimingDelay !=0);
}
 



/*==== ADC set up ====*/
// http://homepage.cem.itesm.mx/carbajal/Microcontrollers/SLIDES/STM32F3%20ADC.pdf
// https://community.st.com/s/question/0D50X00009XkgZz/stm32f3-adc-in-differential-mode
// https://www.youtube.com/watch?v=qqGsy06mris&t=466s
