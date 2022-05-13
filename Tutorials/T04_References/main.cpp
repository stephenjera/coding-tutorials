#include <iostream>
using std::cout;
using std::endl;

int main(void){
    // Declare pointer 
    int* ptr;
    cout << "ptr address: " << ptr << endl;

    // Create an int variables
    int var = 21;
    int foo = 42;

    // Print garbage since pointer point to nothing
    cout << "Value at ptr: " << *ptr << endl;

    // Pointer now points to var 
    ptr = &var;

    // Output value at var
     cout << "Updated value at ptr: " << *ptr << endl;

    // Pointer now points to foo 
    ptr = &foo;

     // Output value at foo
     cout << "Value at foo: " << *ptr << endl;

    /************************************************
    * A reference gives a variable a different name *
    * and it keeps its old one                      *
    /************************************************/

    // Declare reference
    int& ref = var;  

    cout << "Value at ref: " << ref << endl;
    cout << "value at var: " << var << endl;


    return 0;
}