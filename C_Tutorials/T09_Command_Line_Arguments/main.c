#include <stdio.h>
enum{
    questionMark = 63  // ASCII number for question mark 
};

void help(){
     printf("This command line tool takes strings and ");
     printf("converts them into a comma separated list\n");
}

int main(int arg, char *arr[])
{
    // Arg stores the number of arguments 
    // arr stores pointers to the arguments 
    // First position is reserved for the file name 
    printf("file name: %s\n", arr[0]);
    printf("number of arguments: %d\n", arg-1);
    // arg > 1 because 0 is file name 
    if(arg > 1){
        // arr > 1 because 0 is file name
        if(*arr[1] == questionMark){
            help();
        } else {
            // arg > 1 and arr[1] is not a question mark
            for (int i = 1; i < arg; ++i){
                //printf("arg: %d index: %d", arg, i);
                printf("%s", arr[i]);
                if(i != arg-1){
                    // If not at the position before last argument add a comma
                    printf(", ");
                }
             }
        }
    } else {
        printf("No arguments given\n");
        help();
    }

    return 0;
}
