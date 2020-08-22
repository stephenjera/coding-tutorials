// An example of pointers to characters
#include <iostream>
using namespace std;

// prototype of function to add together three numbers
void AddNumbers(int, int&, int*);

int main()
{
	char* ChPoint; // Declare pointer to hold address
	char Ch; // Declare varaible 
	ChPoint = &Ch; // Assign the address of ch to pointer varaible 
	Ch = 'A'; // Assign 'A' to Ch variable 
	cout << *ChPoint << endl; // Output the contents pointed to by the address
	*ChPoint = 'B';
	cout << *ChPoint << endl;
	Ch = 'C';
	cout << *ChPoint << endl << endl;

	// Creating an integer pointer 
	int* p; // Declare pointer variable 
	int Integer; // Declare integer varaible
	p = &Integer; // Assign p the address of integer 
	*p = 12; // Assign 12 to 

	// Both output the same value 
	cout << Integer << endl;
	cout << *p << endl << endl;;

	// Playing with pointers 
	int Integer1 = 4, Integer2 = 5, Integer3 = 6; // Declare and intials 3 interger 
	int* IntegerPointer1; // Create two integer pointers 
	int* IntegerPointer2;

	IntegerPointer1 = &Integer1; // Assign address to pointer
	*IntegerPointer1 = Integer2 + Integer3; // Assign sum to Integer1
	cout << *IntegerPointer1 << endl; // Print sum in Integer1

	IntegerPointer2 = &Integer2; // Assign address to pointer
	*IntegerPointer2 = Integer2 + Integer3; // Assign sum to Integer2
	cout << *IntegerPointer1 * *IntegerPointer2 << endl; // Print product of Integer1 and Interger2 

	IntegerPointer1 = &Integer3; // Assign address to pointer
	*IntegerPointer2 = Integer1 + Integer3; // Assign sum to Integer2
	cout << *IntegerPointer1 * *IntegerPointer2 << endl; // Print product of Integer3 and Interger2
	cout << Integer1 << " " << Integer2 << " " << Integer3 << " " << endl; //Print values in integer varaibles 

	// Using AddNumbers function
	int Num1, Num2, Num3;
	// Obtain values for Num1, Num2 and Num3 from the user
	cout << "Choose three numbers, press enter after each." << endl;
	cin >> Num1 >> Num2 >> Num3;

	// Call the function AddNumbers here
	AddNumbers(Num1, Num2, &Num3);
	// Display the answer here
	cout << "sum: " << Num3 << endl; // Num3 was modified by the function as address was passed

	return 0;
}

void AddNumbers(int a, int& b, int* c)
{
	// Add the numbers and store the answer in c
	// Need to dereference c as its an address
	*c = a + b + *c; 
}