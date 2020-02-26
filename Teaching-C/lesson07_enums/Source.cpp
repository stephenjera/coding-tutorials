#include <iostream>
#include <string.h>
using namespace std;

enum Choice
{
	EASY = 1,
	MEDIUM = 2,
	HARD = 3
};
int main() {
	int i = -1;

	// ...<present the user with a menu>...
	cout << "Please type a number between 1 and 3 \n";
	cin >> i;

	switch (i)
	{
	case EASY:
		cout << "Easy\n";
		break;
	case MEDIUM:
		cout << "Medium\n";
		break;
	case HARD:
		cout << "Hard\n";
		break;
	default:
		cout << "Invalid Selection\n";
		break;
	}
}