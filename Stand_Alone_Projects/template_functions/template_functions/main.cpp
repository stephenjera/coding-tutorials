#include <iostream>

template <class T, class U>  // Why does this work?
T calculate(T a, U b) {
	std::cout << a + b << std::endl;
	std::cout << a - b << std::endl;
	std::cout << a * b << std::endl;
	std::cout << a / b << std::endl;
	//std::cout << a % b << std::endl;
	return 0;
}

int main(void) {
	calculate(2.4, 5);
}

