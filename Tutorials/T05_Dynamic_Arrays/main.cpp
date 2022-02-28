#include <iostream>
using std::cin;
using std::cout;

int main(){
    // Declare variables 
    int size;

    // Get user input for size
    cout << "Enter array size: ";
    cin >> size;

    // Create dynamic array 
    int* arr = new int[size];

    // Populate array 
    for(int i = 0; i < size; ++i){
        cout << "Enter a number\n";
        cin >> arr[i];
    }

    // Print array 
    for(int i = 0; i < size; ++i){
        cout << arr[i] << "  ";
    }

    // Deallocate memory for dynamic array 
    delete[]arr;
    // Ensure pointer is not pointing to random address
    arr = NULL; 

    return 0;
}