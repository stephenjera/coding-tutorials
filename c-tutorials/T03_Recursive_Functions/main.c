// Compiled with "gcc -O0 main.c"
#include <stdio.h>

int func1(int num)
{
if (num==1) return 1 ; // Exit or base condition which gives an idea when to exit this loop
return num*fun(num-1); // Function is called with num-1 as it's argument
//The value returned is multiplied with the argument passed in calling function
}

// This function will crash since it doesn't have an exit condition
int func1(int a) {
    return func1(a+1);
}

int main(void) {
    printf("Starting");

    int test = 4;
    int result = 0;
    result =func1(test);
    printf("%d\n",result);//prints the output result.

    printf("%i\n", func2(0));
}