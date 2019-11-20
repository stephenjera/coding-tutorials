#include <iostream>
/*
Little Mac is an interplanetary space boxer, who is trying to win championship 
belts for various weight categories on other planets within the solar system.
Write a space.cpp program that helps him keep track of his target weight
*/

// Planet weight scalar
constexpr auto venus = 0.78;
constexpr auto mars = 0.39;
constexpr auto jupitar = 2.65;
constexpr auto saturn = 1.17;
constexpr auto uranus = 1.05;
constexpr auto neptune = 1.23;

int main() {

	int weight;
	int planet = -1; // Where the fight takes place
	
	// Get user weight
	std::cout << "What is your Earth weight in Kg?\n ";
	std::cin >> weight;

	// Error check 
	do {
		// Get target planet 
		std::cout << "What planet do you want to fight on?\n";
		std::cout << "1: Venus\n 2: Mars\n 3: Jupitar\n 4: Saturn\n 5: Uranus\n 6: Neptune\n";
		std::cout << "chose a number and press ENTER\n";
		std::cin >> planet;
	} while (planet > 6 || planet < 1);
	
		switch (planet) {
		case 1:
			weight - (weight *= venus);
			break;
		case 2:
			weight - (weight *= mars);
			break;
		case 3:
			weight - (weight *= jupitar);
			break;
		case 4:
			weight - (weight *= saturn);
			break;
		case 5:
			weight - (weight *= uranus);
			break;
		case 6:
			weight - (weight *= neptune);
			break;
		default:
			std::cout << "Error check is not working";

		}

		std::cout << "Your target weight is: " << weight << "Kg.\n";
	
}