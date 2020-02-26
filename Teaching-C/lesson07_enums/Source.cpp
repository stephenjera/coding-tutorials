#include <iostream>
using namespace std;

// Declaring some Enums 
enum direction { East, West, North, South };

int main() {
	
	int dir = East; 
	int dir2 = West; 
	cout << "Dir = " << dir << endl;
	cout << "Dir2 = " << dir2 << endl;
	cout << "Pick a direction" << endl;
	cin >> dir;

	if (dir = East) {
		cout << "You entered East" << endl;
	}
	else {
		cout << "Enum failed" << endl; 
	}
	
}
