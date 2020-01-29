#include <iostream>
#include <stdio.h>

/*Bitwise operators
* not = ~
* and = &
* or  = |
* xor = ^
* Left shift = <<
* Right shift = >>
*/

uint16_t a = 0x0000;
uint16_t b = 0x1001;


int main(void) {
	std::cout << (a | b) << std::endl; // Print in decimal 
	printf("(a | b) = (0x%04x | 0x%04x) = 0x%04x", a, b, (a | b)); // Print in hex
}