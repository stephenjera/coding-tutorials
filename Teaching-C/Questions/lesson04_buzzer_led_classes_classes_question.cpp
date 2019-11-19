#include <iostream>

//Buzzer class
class Buzzer {
public:
	// Buzzer setter 
	void setBuzzer(bool p) {
		power = p;
	}
	// Buzzer getter
	bool getBuzzer() {
		return power;
	}
private:
	bool power;
};

// Create a LED class 


// The main function of the washing machine 
class Process {
public:
	// Class constructor 
	// Member initialisation
	Process(Buzzer b, Led l) : buzzer(b), ledPower(l){
		std::cout << "Let's begin:" << std::endl;
	}
	// Class destructor 
	~Process() {
		std::cout << "The end is now!" << std::endl;
	}
	// Door setter 
	void setDoor(bool d) {
		door = d;
	}
	// Door getter 
	bool getDoor() {
		return door;
	}
private:
	bool door;
	Buzzer buzzer; // Buzzer composition 
	Led ledPower;
};


int main(void) {
	Buzzer buzzer;
	buzzer.setBuzzer(true); 

	Led ledPower; 
	ledPower.setLed(false);

	Process start(buzzer,ledPower); // Creating an object, takes an object as it's argument
	start.setDoor(true); // Calling setDoor function 

	// Checking values
	bool doorOutput = start.getDoor(); // Initialising output with door value
	bool ledOutput = ledPower.getLed();
	bool buzzerOutput = buzzer.getBuzzer();
	std::cout << "The door is: " << doorOutput << std::endl;
	std::cout << "The led is: " << ledOutput << std::endl;
	std::cout << "The door is: " << buzzerOutput << std::endl;

	// Making outputs more meaningful 
	// Using if statements make the code below "Checking values" easier 
	// to understand in the consle output.
}