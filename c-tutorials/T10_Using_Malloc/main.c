// Write a function that returns every multiple of 3 between 0 and 100.
#include <stdio.h>
#include <stdlib.h>

// used to return multiple values from function
typedef struct values{
    int* pArray;
    int size;
} t_values;

t_values multiples3(){
    // malloc returns pointer to memory block
    int* arr = malloc(100*sizeof(int));
    int count = 0;
    int i;
    for(i = 0; i <= 100; i++){
        if(i % 3 == 0){
            arr[count] = i;
            count++;
        }
    };
    // arr is a point so function returns a pointer
    t_values val;
    val.pArray = arr;
    val.size = count;
    return val;
}

int main(){
    t_values newArr = multiples3();
    //printf("size of newArr %d value: %d", newArr.size, newArr.pArray[2]);
    // print arrary 
    for(int i; i < newArr.size; i++){
        printf("index: %d value: %d \n", i, newArr.pArray[i]);
    } 
    return 0;
}