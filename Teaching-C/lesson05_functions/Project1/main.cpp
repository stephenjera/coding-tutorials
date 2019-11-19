#include <iostream>
//#include <math.h>

constexpr auto sqrd = 2;

// Function prototypes 
int sum(int a, int b);

// Create a function that finds the hypotenuse of a right angle triangle
float hypotenuse(float len1, float len2);

 void main() { 

	float result = hypotenuse(3, 4);
	int summ = sum(1, 2);

	std::cout << "The sum is: " << summ << std::endl;
	std::cout << "The hypotenuse is: " << result << std::endl;

}

// Function definitions
 int sum(int a, int b) {
	 return a + b;
 }

 float hypotenuse(float len1, float len2) {
	 return sqrt((len1 * len1) + (len2 * len2));
	 //return sqrt(pow(3, sqrd) + pow(4 ,sqrd));
 }

