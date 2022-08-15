// Write a function that returns every multiple of 3 between 0 and 100.

int multiples3(int* arr[], int size){
    int* arr = malloc(100*sizeof(int));
    int count = 0;
    for(int i = 0; i =< 100; i++){
        if(i % 3 == 0){
            arr[count] = i;
            count++;
        }
    }
    return arr;
}