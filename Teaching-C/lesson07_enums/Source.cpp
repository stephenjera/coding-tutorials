#include <iostream>
#include <string.h>
using namespace std;

enum Choice
{
	FILL = 1,
	HEAT = 2,
	WASH_SLOW = 3,
	EMPTY = 4,
	RINSE = 5,
	SPIN_FAST = 6,
	SPIN_SLOW = 7,
	DRY = 8,
	COMPLETE = 9
};
int main() {
	int i = -1;

	// ...<present the user with a menu>...
	cout << "Please type a number between 1 and 9 \n";
	cin >> i;

	switch (i)
	{
	case FILL:
		cout << "FILL\n";
		break;
	case HEAT:
		cout << "HEAT\n";
		break;
	case WASH_SLOW:
		cout << "WASH_SLOW\n";
		break;
	case EMPTY:
		cout << "EMPTY\n";
		break;
	case RINSE:
		cout << "RINSE\n";
		break;
	case SPIN_FAST:
		cout << "SPIN_FAST\n";
		break;
	case SPIN_SLOW:
		cout << "SPIN_SLOW\n";
		break;
	case DRY:
		cout << "DRY\n";
		break;
	case COMPLETE:
		cout << "COMPLETE\n";
		break;
	default:
		cout << "Invalid Selection\n";
		break;
	}
}