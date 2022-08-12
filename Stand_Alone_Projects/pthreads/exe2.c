#include<stdio.h>
#include<pthread.h>

int main()
{
    printf("Hello\n");
    pthread_exit("Bye");
    printf("Hello again");
    return 0;
}