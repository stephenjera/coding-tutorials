#include <iostream>
#include <string>

// Class declaration
class Student {
public:
	// Create constructor
	Student(std::string nm) {
		set_name(nm);
		std::cout << "Your name is " << nm << std::endl;
	}
	// function to set the name
	void set_name(std::string x) {
		name = x;
	}
	// Function to display the name
	std::string get_name() {
		return name;
	}
private:
	std::string name;
};

class Washing_Machine {
public:
	void spin_to_win() {
		std::cout << "I'm a washing machine" << std::endl;
	}
};

int main() {
	// Testing constructor 
	Student one("Jing Xi Yang");
	one.set_name("I changed your name");
	std::cout << one.get_name() << std::endl;

	// Testing washing machine 
	Washing_Machine test;
	test.spin_to_win();
}