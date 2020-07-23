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
    char buff[255] = "0";
    char searchText[8][2];
    //char searchText[6][3]; // Known from file
    FILE *fp;

    fp = fopen(search1, "r");
    if(fp == NULL)
    {
        perror("Unable to open file");
        exit(1);
    }
    int row = 0,col = 0;
    // fgets(variable to store line, size of line(int),file pointer)
    /*while(fgets(buff,sizeof(buff),fp))
    {
        printf("%s",buff);
        searchText[row][col] = buff;
        row++;
    }*/
    // COULD READ FIRST LINE AND CHECK THE ARRAY FOR IT
    // THEN READ NEXT LINE
    fgets(buff,sizeof(buff),fp);
    printf("%s",buff);

    searchText[0][0] = buff[0];
    searchText[0][1] = buff[1];
    searchText[0][2] = buff[2];

    /*
    fgets(buff,sizeof(buff),fp);
    printf("%s",buff);
    fgets(buff,sizeof(buff),fp);
    printf("%s",buff);
    fgets(buff,sizeof(buff),fp);
    printf("%s",buff);
    fgets(buff,sizeof(buff),fp);
    printf("%s",buff);
    fgets(buff,sizeof(buff),fp);
    printf("%s",buff);
    fgets(buff,sizeof(buff),fp);
    printf("%s",buff);
    fgets(buff,sizeof(buff),fp);
    printf("%s",buff);*/
   /* fscanf(fp, "%s", puzzleText); // Doesn't read white space
    printf("1 : %s\n", puzzleText);
    */
    fclose(fp);
    printf("\nFile closed\n");
    // ARRAY ONLY SAVES LINE READ LAST
    /*int i = 0;
    for(i ;i <= sizeof(searchText); i++)
    {
        //printf("%c",buff[i]);
        printf("%c",searchText[i][col]);
    }*/
    printf("%c",searchText[0][0]);
    printf("%c",searchText[0][1]);
    printf("%c",searchText[0][2]);

    return 0;
}
