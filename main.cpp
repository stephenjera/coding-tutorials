/* The creation of the rock paper scissors game */

#include <iostream>
#include <string.h>
#include <time.h>
using namespace std;

// Constant definitions 
#define MAX 3  // Used for rand number generation
#define MIN 1  // Used for rand number generation
#define ROCK 1
#define PAPER 2
#define SCISSORS 3

// Funtion prototypes 
int rand_num();  // Generates a random number within a range
void rock_paper(); // Starts the game 

int main() {
	rock_paper();  // Lets play the game
	return 0;
}

// Function definitions 
int rand_num() {
	srand(time(0));  // Set srand to get random number each run of code
	int range = MAX - MIN + 1;  //  <-- LOOK INTO HOW THIS FORMULA WORKS
	int num = rand() % range + MIN;  //  <-- LOOK INTO HOW THIS FORMULA WORKS
	return num;
}

// Function for the game
void rock_paper() {
	// Variable definitions
	int user_choice;
	int cpu_choice = rand_num();
	//cout << "The cpu chose: " << cpu_choice << "\n\n";  // Debugging line

	// Getting the user input 
	cout << "what would you like to throw? \n";
	cout << "For rock press: 1 then ENTER \n";
	cout << "For paper press: 2 then ENTER \n";
	cout << "For scissors press: 3 then ENTER \n";
	cin >> user_choice;

	if (cpu_choice == user_choice) {  // Check for draw 
		cout << "DRAW \n\n";
	} else {
		// Need a better implementation 
		/* For impossible game change "==" to "=", user will never win*/
		switch (user_choice) {
		case ROCK:  // Rock
			if (cpu_choice == PAPER) {
				cout << "The cpu chose: " << cpu_choice << "\n\n";  // Debugging line
				cout << "Better luck next time. \n\n";
			}
			else {
				cout << "The cpu chose: " << cpu_choice << "\n\n";  // Debugging line
				cout << "Congrats you beat the super AI! \n\n";
			}
			break;
		case PAPER:  // Paper
			if (cpu_choice == SCISSORS) {
				cout << "The cpu chose: " << cpu_choice << "\n\n";  // Debugging line
				cout << "Better luck next time. \n\n";
			}
			else {
				cout << "The cpu chose: " << cpu_choice << "\n\n";  // Debugging line
				cout << "Congrats you beat the super AI! \n\n";
			}
			break;
		case SCISSORS:  // Scissors
			if (cpu_choice == ROCK) {
				cout << "The cpu chose: " << cpu_choice << "\n\n";  // Debugging line
				cout << "Better luck next time. \n\n";
			}
			else {
				cout << "The cpu chose: " << cpu_choice << "\n\n";  // Debugging line
				cout << "Congrats you beat the super AI! \n\n";
			}
			break;
		default:
			break;

		}
	}

}