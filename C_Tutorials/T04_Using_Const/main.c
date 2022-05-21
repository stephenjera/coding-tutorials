#include <stdio.h>

int main(){
    // Const means a variable is read only 
    const int constInt = 0;  // Constant integer 
    int const constInt2;  // Constant integer
    const int *constInt3;  // Constant integer variable pointer 
    int * const constPtr;  // Constant integer pointer variable integer 
    const int const * constIntPtr;  // Constant integer pointer constant  integer 

    // Value can still be changed if address is changed 
    int* ptr = &constInt;
    printf("Inital value: %d \n", constInt);
    *ptr = 5;
    printf("Value after changing with pointer: %d \n", constInt);

    return 0;
}