#include <stdio.h>
#include <stdlib.h>

/*
    Use "text1.txt" as your puzzle file.
•	The list of search words is in "search1.txt".
•	Read in the text file "text1.txt". You should read the characters into an array.
•	Read in the text file "search1.txt" You should read the characters into an array.
•	Do a comparison between the words from "search1.txt" and the words from "text1.txt".
    You need to find the occurrence of each word from “search1.txt” in the string of characters from “text1.txt”.
    Not all of the words occur in “text1.txt”.
•	Output the word, whether it has been found and, if found, the index of its location in the array,*/

// Puzzle text file
const char* text1 = "C:/A/Intern-Pre-Work/text1.txt";
// List of search words
const char* search1 = "C:/A/Intern-Pre-Work/search1.txt";

int main()
{
    printf("Hello world!\n");
    char puzzleText[255];
    char searchText[6][3] // Known from file
    FILE *fp;

    fp = fopen(text1, "r");
    fscanf(fp, "%s", puzzleText); // Doesn't read white space

    printf("1 : %s\n", puzzleText);
    //printf("%c\n",buff[3]);

    fclose(fp);
    return 0;
}
