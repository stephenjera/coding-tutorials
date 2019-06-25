/*Will contain multiple examples of working with strings*/

#include <iostream>
#include <string>
#include <string.h>
#include <cctype>

using namespace std;
// function prototypes
void Change_Case(); // Takes a string and changes a letter to different case

int main() {
	// Change in case 
	Change_Case(); // Run the function 
	return 0;
}

// Function definitions
void Change_Case() {
	/*//////////////////*/
	/*ADD ERROR CHECKING*/
	/*//////////////////*/
	string Input; // String to change 
	char Output;
	int Len;	  // String size
	int Index;	  // Letter to be changed 

	// Choose a string 
	cout << "Please enter the string" << "\n\n";
	cin >> Input;
	Len = Input.length();

	// Choose letter to change
	cout << "Which letter index should be changed?" << "\n";
	cout << "Choose a number between 0 and " << Len - 1 << "\n\n";
	cin >> Index; 
	
	// Print the result 
	Output = toupper(Input[Index]); // Convert index letter to uppercase
	Input[Index] = Output;			// Replace origional letter in string
	cout << "Your new word is: " <<  Input << "\n\n";
}