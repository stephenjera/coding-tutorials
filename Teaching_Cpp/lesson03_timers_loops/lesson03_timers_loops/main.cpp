#include <iostream>
#include <ctime>

#define HIGHESTNUM 10
#define LOWESTNUM 1
#define TIMER 15

int main(void) {
	// Initialising variables
	int x = 0;
	int y = 0;
	time_t t = time(NULL) + TIMER;

	while (time(NULL) < t) {
		std::cout << t - time(NULL) << " Seconds left!" << std::endl; // Not a reliable count, but good enough
		std::cout << "Choose number before time runs out." << std::endl;
		std::cin >> y;
	}

	do {
		std::cout << "Choose a number between 1 and 10: " << std::endl;
		std::cin >> x;
	} while (x > HIGHESTNUM or x < LOWESTNUM);
	// Bad coding, just illustrating nested if statements 
	if (x >= 7) {
		std::cout << "Your number is seven or bigger." << std::endl;
		if (x >= 9) {
			std::cout << "Your number is nine or bigger." << std::endl;
			// Random count down for loop
			for (int i = 10; i >= 1; i--) {
				std::cout << i << std::endl;
			}
		}
	}
	else {
		std::cout << "your number is: " << x << std::endl; // Number is less than 7 
	}
}