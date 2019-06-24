# include <iostream>
using namespace std;

int main() {
	// cout means console out 
	// endl means end line 
	cout << "Hello World! \n" << endl;

	/*pointers to characters*/
	//char Ch;  /*position does not change much*/
	char* ChPoint; // pointer to a char
	char Ch;

	//cout << "The address of ChPoint is: " << ChPoint << endl;  /*ChPoint is not initialised*/
	cout << "The address of ChPoint is: " << &ChPoint << endl;
	cout << "The address of Ch is : " << &Ch << endl; // returns trash
	ChPoint = &Ch; // address of operator "&" returns address 
	cout << "The address of ChPoint is: " << &ChPoint << endl;
	cout << "The address of ChPoint is: " << ChPoint << endl; // returns trash
	cout << "The address of Ch is : " << Ch << endl << endl; // returns trash

	Ch = 'A';
	cout << *ChPoint << endl; // "*" indirection operator: returns the value stored at address

	*ChPoint = 'B';           
	cout << *ChPoint << endl; // print the contents of ChPoint

	Ch = 'C';
	cout << *ChPoint << endl << endl;


	int Num;
	int* pNum; // holds an address of an integer
	pNum = &Num; // make the address that of Num
	Num = 3;
	cout << "Integer Num is stored at " << pNum; // prints address
	cout << " and has a value of " << *pNum << "\n\n";	 // prints number
	return 0;
}
