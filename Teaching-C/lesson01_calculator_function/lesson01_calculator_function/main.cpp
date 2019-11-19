#include <iostream>

// This is a function prototype 
void calculator(int x, int y);
void calculator(float x, float y); // Example of function overloading

int main() {
	// Defining variables 
	float x_val, y_val;

	std::cout << "Enter X value then press enter: " << std::endl; // Printing to console
	std::cin >> x_val; // Getting value from user 
	std::cout << "Enter Y value then press enter: " << std::endl;
	std::cin >> y_val;

	calculator(x_val, y_val); // Calling a function 

}

// This is a function definition 
void calculator(int x, int y) {
	// Print to console 
	std::cout << "Sum of addition is: " << x + y << std::endl;
	std::cout << "Difference of subtraction is: " << x - y << std::endl;
	std::cout << "Product of multiplication is: " << x * y << std::endl;
	std::cout << "Quotient of division is: " << x / y << std::endl;
}
void calculator(float x, float y) {
	// Print to console 
	std::cout << "Sum of addition is: " << x + y << std::endl;
	std::cout << "Difference of subtraction is: " << x - y << std::endl;
	std::cout << "Product of multiplication is: " << x * y << std::endl;
	std::cout << "Quotient of division is: " << x / y << std::endl;
}