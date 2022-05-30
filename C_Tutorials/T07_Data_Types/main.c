#include <stdio.h>
#include <stdint.h>
#include <ctype.h>

// Primitive data types are built into the language 

int main(){
    // All data in memory is binary and data types represent the number of bits used to represent a variable 
    // Type declarations are the standard of how those binary numbers will be interpreted 
    printf("An int reserves %d bytes of memory\n", sizeof(int));
    printf("An int16 reserves %d bytes of memory\n", sizeof(int16_t));
    printf("A short size: %d bytes is the same as int16_t size %d bytes\n", sizeof(short), sizeof(int16_t));
    printf("A char size: %d bytes is the same as int8_t size: %d bytes\n", sizeof(char), sizeof(int8_t));
    printf("An unsigned int %d bytes is the same size as a signed int %d bytes\n", sizeof(unsigned int), sizeof(signed int));
    printf("A long is size: %d bytes\n", sizeof(long));
    printf("A long long is size: %d bytes\n", sizeof(long long));

    char a = 'a';
    // Array of size 3 present interesting behaviour 
    char b[4] = {'b','o','o'};

    printf("a: %c, b: %s\n", a, b);
    for(int i=0; i <= 4; i++){
        // Check if last element in array is a space
        if(isspace(b[i])){
            // It's not a space it prints 'a' to the console 
            printf("space");
        } else {
            printf("%c", b[i]);
        }
    }
}