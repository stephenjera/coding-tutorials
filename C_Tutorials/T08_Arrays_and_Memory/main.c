#include <stdio.h>
#include <stdint.h>
#include <ctype.h>

#define null '\000'  // ASCII code for NULL character 

int main(){
    char a = 'a';
    char b[4] = {'b','o','o'};

    // Print variable values 
    printf("a is: %c, b is: %s\n", a, b);
  
    // Check the uninitialised element of the array 
    if(b[3] == null){
        printf("b[3] is NULL");
    } else {
        // Should be null so should never get here 
        // if not null then is garbage 
        printf("b[3] is: %d\n", b[3]);
    }

    // Deliberately go outside of defined space for array
    // Results may vary, compiler doesn't stop you accessing memory you shouldn't 
    for(int i = 0; i < 10; i++){
        // Check if element in array is a space
        if(isspace(b[i])){
            printf("\nspace");
        }
        // Compiler complains about using NULL since it's a pointer 
        else if(b[i] == null){
            printf("\n Is NULL");
        } else {
            printf("\n%c", b[i]);
        }
    }
}
