#include <stdio.h>

// Limit scope of variable to file
static int globalStatic; 

// Static variables have a property of preserving their 
// value even after they are out of their scope
void foo(){
    //Remains in memory while program is running 
    // Memory allocated in data segment
    static int isStatic = 10; 

    // Destroyed when out of scope 
    // Memory allocated in stack 
    int notStatic = 10;
   

    notStatic += 1;
    isStatic += 1;   

    printf("Not static: %d ", notStatic);
    printf("Is static: %d\n", isStatic);
}

int main(){
    for(int i = 0; i < 10; ++i){
        // Keeps value from last function call
        foo();
    }

    foo();

    // Static int is initialised to 0
    printf("Global static: %d", globalStatic);

    return 0;
}