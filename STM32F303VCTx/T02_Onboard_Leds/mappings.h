//#ifndef 
//#include "stm32f3xx.h"  // Device header

// Macros for LEDS 3 - 10
unsigned int       SET_BIT = 0b00000000000000000000000100000000;
#define LD_ALL_ON  0x0000FF00;
#define LD_ALL_OFF 0xFF000000;
#define LD3_ON     SET_BIT << 1;
#define LD4_ON     SET_BIT;
#define LD5_ON     SET_BIT << 2
#define LD6_ON     SET_BIT << 7;
#define LD7_ON     SET_BIT << 3;
#define LD8_ON     SET_BIT << 6;
#define LD9_ON     SET_BIT << 4;
#define LD10_ON    SET_BIT << 5;





//#endif