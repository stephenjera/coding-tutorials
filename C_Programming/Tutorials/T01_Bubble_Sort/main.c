#include <stdio.h>
#define SIZE_OF_ARRAY   (10)

void sort(int* const data, const int arraySize) {
  /* TODO: implement any sort algorithm to sort a given array of integer.
  Note: feel free to change the function signature and return type to suit.
  */

 // Loop to get element of array to compare with
 for (int i=0; i<arraySize; i++) {
     int temp = 0;  // Variable to temporarily store a value to 
     // Loop through to compare value in first loop against all values in array 
     for (int j=0; j<arraySize; j++) {
         // Swap values 
         if(data[i] < data[j]){
            // Magic math trick 
            data[i] = (data[i] + data[j]) - (data[j] = data[i]);
            /*
            temp = data[i];  
            data[i] = data[j]; 
            data[j] = temp;
            */
         }
            
     }
 }

}

void debugPrintArray(int const * const data, const int arraySize) 
{
    printf("========= \n");
    for (int i=0; i<arraySize; i++) {
        printf("%d, ", data[i]);
    }
    printf("\n========= \n\n");
}

int main()
{
    int data[SIZE_OF_ARRAY] = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3};
 
    printf("Unsorted array: \n");
    debugPrintArray(data, SIZE_OF_ARRAY);
    
    // TODO: we want to sort the data array here.
    sort(data, SIZE_OF_ARRAY);

    printf("Sorted array: \n");
    debugPrintArray(data, SIZE_OF_ARRAY);
    return 0;
}