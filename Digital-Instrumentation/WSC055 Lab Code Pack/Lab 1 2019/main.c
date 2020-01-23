  /* 
	Pete Hubbard 2019
	Loughborough University
	WSC055 Lab 1
	V.2.0
	
	The following 'c' code presents an outline for you to adapt during the laboratory
	
	*/

#include "stm32f3xx.h"                  // Device header


#define SysClk 8000000 // Assumed system clock from trial & error, unclear writing on oscillator crystal, and hopefully datasheet
#define PreScaler 7999 // Theo added #define's these to make life easier.
#define AutoReloadReg 999 // PSC(7999) & ARR(999) on 8MHz clk gives 1s. 10 on latter gives 0.01s

#define USER GPIOA->IDR

/* GLobal variables */
int counter = 0xFF; 
int start   = 0;
uint32_t test = 0;
int nottest = 0;
int flash = 0xFF;
float adc_voltage = 0;

// https://www.badprog.com/electronics-stm32-using-the-push-button-to-switch-on-the-led6-on-the-stm32f3-discovery-board 

/* Function prototypes */
void delay(int a); 
void TIM3_IRQHandler(void);
void DAC_setup(void);
void LED_setup(void);
void IRQ_setup(void);
void ADC_setup(void);
float read_ADC(void);

int main(void)
 {
	LED_setup();
	IRQ_setup(); // timer interrupt
	DAC_setup();
	ADC_setup();
		
	// Main programme loop 
	while (1) {
		
		if (USER & 0x1) {
//			GPIOE->BSRRH = 0xff00; // turn off all bits 
//			adc_voltage = read_ADC();
//			counter = (int)(((double)3.3) / adc_voltage * 256);
//			counter &= 0xFF;
		  //IRQ_setup(); // timer interrupt
			
//			while(counter) {	
//				GPIOE->BSRRL =  counter << 8; // Bit set register (BSRRL) L = set low
//				delay(1*1000000); // On time  // Can't get accurate time with this method
//				GPIOE->BSRRH =  counter << 8; 
//				counter--; 
//				}
//			
//			for (int i = 20; i > 0; i--){
//				GPIOE->BSRRL =  flash << 8; // Bit set register (BSRRL) L = set low
//				delay(1*100000); // On time  // Can't get accurate time with this method
//				GPIOE->BSRRH =  flash << 8; 
//				flash = flash * 2;			
//			}		
		} else {
			adc_voltage = read_ADC();
			GPIOE->BSRRH = 0xff00; // turn off all bits 
			GPIOE->BSRRL = (int)(((double)3.3) / adc_voltage * 256) << 8;
		}
	}
}

// Delay function to occupy processor
void delay (int a) // takes micros
{
    volatile int i,j;

    for (i=0 ; i < a ; i++)
    {
        j++;
    }

    return;
}

int interruptCount = 0x0000 - 0x0100; // essentially -512. Could also use an unsigned char/byte cause I'm not using much
int delayCount = 0;
int TEN_SECONDS = 10 / ( ((PreScaler+1) * (AutoReloadReg+1)) / (float)SysClk ); // 10 divided by interrupt time. Will always be number of ISR ticks for 10s!

void TIM3_IRQHandler() {
	if ((TIM3->SR & TIM_SR_UIF)) {// Check interrupt source is Update Interrupt
		
		GPIOE->BSRRH =  counter << 8; 
		counter--;
		GPIOE->BSRRL =  counter << 8; // Bit set register (BSRRL) L = set low
		
	}
  TIM3->SR &= ~TIM_SR_UIF; // Clear UIF
}


void DAC_setup() {

  RCC->APB1ENR |= RCC_APB1ENR_DAC1EN;
  DAC1->CR |= DAC_CR_BOFF1; // Disable the ‘buffer’ function in the DAC control register
  DAC1->CR |= DAC_CR_EN1; // Enable DAC peripheral

}

void LED_setup() {
	// Enable clock on GPIO port E
	RCC->AHBENR |= RCC_AHBENR_GPIOEEN;
	GPIOE->MODER |= 0x55550000; // Set mode of pins 8-15 (LEDs on circle) in port E to 'Output'
	GPIOE->OTYPER &= ~(0xff00); // Set output type for LED pins to 'Open Drain'
	GPIOE->PUPDR &= ~(0x55550000); // Set Pull up/Pull down resistor configuration for LEDs
}

void IRQ_setup() {
	
	RCC->APB1ENR |= RCC_APB1ENR_TIM3EN;
	TIM3->PSC = PreScaler; // 7999 ~8k
	TIM3->ARR = AutoReloadReg; // 999 ~1k

	TIM3->CR1 |= TIM_CR1_CEN; // Seen here in Pete's notes & once online
	TIM3->DIER = TIM_DIER_UIE;
	NVIC_EnableIRQ(TIM3_IRQn);
}

void ADC_setup() {
  RCC->CFGR2 |= RCC_CFGR2_ADCPRE12_DIV2; // Configure the ADC clock
  RCC->AHBENR |= RCC_AHBENR_ADC12EN; // Enable ADC1 clock
  ADC1_2_COMMON->CCR |= 0x00010000; // url had alt. weird error-checking-if-statement instead of this line from Pete
	
	// Enable Voltage regulator
	ADC1->CR &= ~ADC_CR_ADVREGEN; // set ADVREGEN[1:0](pin 29 & 28) to 0 - (page 22). Alt, (0b11 << 27)
  ADC1->CR |= ADC_CR_ADVREGEN_0; // 01: ADC Voltage regulator enabled
	delay(10); //Delay(10); // Insert delay equal to 10 µs
	
  ADC1->CR &= ~ADC_CR_ADCALDIF; // calibration in Single-ended inputs Mode i.e. set to 0. (page 27)
  ADC1->CR |= ADC_CR_ADCAL; // Start ADC calibration
  
  // Read at 1 means that a calibration in progress.
  while (ADC1->CR & ADC_CR_ADCAL); // wait until calibration done
  //int calibration_value = ADC1->CALFACT; // Get Calibration Value ADC1. Nice-to-have but not used
  
	RCC->AHBENR |= RCC_AHBENR_GPIOAEN;
	GPIOA->MODER |= 0x0000008; // Set mode of pin PA0 to '10' for 'Analogue' (see on page 19 in basic Microcontroller Ports lecture)
	
	// 5. Configure ADC using the ADCx_CFGR register to have
	ADC1->CFGR &= ~ADC_CFGR_CONT; // ADC_NonContinuousConvMode_Enable
  ADC1->CFGR |= ADC_CFGR_RES_1; // 8-bit data resolution...
	ADC1->CFGR &= ~ADC_CFGR_RES_0; // Can't be done in 1 instr cause not same value
  ADC1->CFGR &= ~ADC_CFGR_ALIGN; // Right data alignment
	
  //    while(!ADC1->ISR & ADC_ISR_ADRD); // wait for ADRDY
  ADC1->SQR1 |= ADC_SQR1_SQ1_1; // SQ1 = 0x01, start converting ch1  USE PA1
  ADC1->SQR1 &= ~ADC_SQR1_L; // ‘L’ (length) = ‘0’ (1 channel only). L's 4 bits but still all turn to 0
  ADC1->SMPR1 |= ADC_SMPR1_SMP7_1 | ADC_SMPR1_SMP7_0; // = 0x03(0b11) => sampling time 7.5 ADC clock cycles, others on page 26
  // 7. Enable the ADC
  // 8. Wait for the ADRDY flag to go ‘high’.
	ADC1->CR |= ADC_CR_ADEN; // Enable ADC1
  while(!ADC1->ISR & ADC_ISR_ADRD); // wait for ADRDY
}

float read_ADC() {
	// 1. Start the conversion by setting the ADSTART bit high
	ADC1->CR |= ADC_CR_ADSTART; // Start ADC1 Software Conversion
	
	// 2. Wait for the end of conversion (reported in the ADCx_ISR register by the EOC bit going high)
  // 3. Read data from the data register (ADCx_DR). Doing this resets the EOC flag.
	while(!(ADC1->ISR & ADC_ISR_EOC)); // Test EOC flag
  int ADC1ConvertedValue = ADC1->DR; // Get ADC1 converted data, returned as 8bit value(or whatever set resolution)
	float ADC1ConvertedVoltage = (ADC1ConvertedValue *3.3)/(float)256; // Compute the voltage, for 8bit, in V
	return ADC1ConvertedVoltage;
}

