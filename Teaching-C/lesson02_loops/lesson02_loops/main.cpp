#include <iostream>

int main() {
	int x;
	do {
		std::cout << "Choose a number between 1 and 10: " << std::endl;
		std::cin >> x;
	} while (x > 10 or x < 1);
	if (x > 5) {
		std::cout << "Your number is bigger than five." << std::endl;
		if (x > 7) {
			std::cout << "Your number is bigger than seven." << std::endl;
		}
	}
	else {
		std::cout << "Your number is less than or equal to five." << std::endl;
	}
}