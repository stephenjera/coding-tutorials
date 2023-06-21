#include <stdio.h>
#include <string.h>

// A struct is a group of variables 
struct Student{
    char name[20];
    char id[5];
    int age;
};

typedef struct Teacher{
        char name[20];
        char id[5];
        int age;
} Teacher;

void printTeacher(Teacher teacher){
    printf("Name: %s\n", teacher.name);
    printf("Id: %s\n", teacher.id);
    printf("Age: %d\n", teacher.age);
}

void printStudent(struct Student student){
    printf("Name: %s\n", student.name);
    printf("Id: %s\n", student.id);
    printf("Age: %d\n", student.age);
}

int main(){
    
    struct Student penny;
    strcpy(penny.name, "Penny");

    // Assign to struct in any order
    struct Student jenny = {.age = 18, .id = "554", .name = "Jenny"};

    // Typedef allows omission of struct keyword 
    // Example of designated initialisation 
    Teacher john = {"John", "1235", 53};

    // Use struct as argument to function
    printTeacher(john);
    printStudent(jenny);
    
    return 0;
}