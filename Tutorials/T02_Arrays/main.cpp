#include <iostream>
using std::cout;
using std::endl;

// Array to print
int arr1[] = {1,2,3,4,5};

// Using arrays as inputs
void printArray(int arr[], int size);


int main(){
    int arrSize = sizeof(arr1)/sizeof(int);
    cout << "Size of array: " << arrSize << endl;
    printArray(arr1, arrSize);

    return 0;
}

// Passing array as pointer loses size information 
// sizeof function retursns size of arry type (e.g int)
void printArray(int arr[], int size){
    cout << arr << endl;
    for(int i = 0; i < size; i++){
        cout << arr[i] << endl;
    }
}
