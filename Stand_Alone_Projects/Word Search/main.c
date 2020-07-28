#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
char puzzleText[20] = "";
char searchText[8][2] = {{""},{""}};

int main()
{
    char buff[255] = "";
    char test[5] = {"cat"};
    int row = 0,col = 0;
    char *ret;
    //char searchText[6][3]; // Known from file
    FILE *fp;

    // Open text1 for reading
    fp = fopen(text1, "r");
    if(fp == NULL)
    {
        perror("Unable to open file");
        exit(1);
    } else
    {
        printf("File opened\n");

        while(!feof(fp)) // While not at the end of file
            {
                //Errors caused by space(CR) at the end of text file
                // fgets(variable to store line, size of line(int),file pointer)
                fgets(buff,sizeof(buff),fp);
                printf("Size of buff: %d\n",sizeof(buff)); // Test line
                printf("Buffer: ");
                printf("%s\n",buff); // Check if buffer has been updated
                printf("Puzzle text: ");
                int j = 0;
                for(j = 0; j < sizeof(puzzleText); j++)
                    {
                        puzzleText[j] = buff[j]; // Save buffer to array
                        // Check if array has bee updated with buffer
                        printf("%c",puzzleText[j]);
                    }
                // ret = strstr(buff,test);
                //printf("The substring is: %s\n", ret);
            }
            fclose(fp);
            buff[255] = ""; //clear buffer
            printf("\nFile closed\n");
    }



    /*
    while(fgets(buff,sizeof(buff),fp))
    {
        printf("%s",buff);
        searchText[row][col] = buff;
        row++;
    }*/
    // COULD READ FIRST LINE AND CHECK THE ARRAY FOR IT
    // THEN READ NEXT LINE
   /* fgets(buff,sizeof(buff),fp);
    printf("%s",buff);


    searchText[0][0] = buff[0];
    searchText[0][1] = buff[1];
    searchText[0][2] = buff[2];*/

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

    // Open search1 for reading
    fp = fopen(search1, "r");
    if(fp == NULL)
    {
        perror("Unable to open file");
        exit(1);
    } else
    {
        printf("File opened\n");
         // fgets(variable to store line, size of line(int),file pointer)
         while(fgets(buff,sizeof(buff),fp))
            {
                printf("%s",buff);
                // ret = strstr(buff,test);
                //printf("The substring is: %s\n", ret);
                for(col = 0; col < sizeof(buff); col++)
                    {
                        searchText[row][col] = buff[col]; // Save buffer to array
                    }
                col = 0;
                row++;
            }
    }

    fclose(fp);
    printf("\nFile closed\n\n");

    // Testing if arrays were written to correctly
    printf("Testing if array was written to correctly\n");
    int j = 0; // CHANGE THE SCOPEOF j FOR THIS LINE TO ACCESS
    for(j = 0; j < sizeof(puzzleText); j++)
        {
            printf("%c",puzzleText[j]);
        }
    printf("\n"); // Formatting line
    //row = 0;
    for(row = 0;row < 8; row++)
        {
            for(col = 0; col < 4; col++)
                {
                    // APPEARS AS IF LAST LETTER NOT WRITTEN CORRECTLY
                    printf("%c",searchText[row][col]);
                }
            printf("\n");
        }


    // ARRAY ONLY SAVES LINE READ LAST
    /*int i = 0;
    for(i ;i <= sizeof(searchText); i++)
    {
        //printf("%c",buff[i]);
        printf("%c",searchText[i][col]);
    }
    printf("%c",searchText[0][0]);
    printf("%c",searchText[0][1]);
    printf("%c",searchText[0][2]);*/

    // CHANGE TO FUNCTION IF WORKS
}

//function to compare array elements
char compareArray(int a[],int b[],int size)	{
	int i;
	for(i=0;i<size;i++){
		if(a[i]!=b[i])
			return 1;
	}
	return 0;
}

