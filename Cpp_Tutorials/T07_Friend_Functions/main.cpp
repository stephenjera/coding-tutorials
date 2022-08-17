/*
Friend functions allow access to private class variables
from without class member functions
*/

#include <iostream>

class Foo {
    public:
        Foo(){
            var = 0;
        }
    private: 
        int var;

    // commenting this line out causes errors 
    // var is private 
    friend void printVar(Foo obj);
    friend void printVar2(Foo &obj);
};

int main(){
    Foo myObj;
    printVar(myObj);

    // won't work because Foo has no member called printVar
    // printVar is a friend function
    //myObj.printVar()

    printVar2(myObj);

}

void printVar(Foo obj){
    obj.var = 74;
    std::cout << obj.var;
}

void printVar2(Foo &obj){
    obj.var = 74;
    std::cout << obj.var;
}
