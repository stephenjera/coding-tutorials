//https://www.c-sharpcorner.com/article/types-of-relationships-in-object-oriented-programming-oops/

#include <iostream>
#include <string>

// Association is a “has-a” type relationship
// but both classes can be independent of each other
// Aggregation is a special form association (one way)
// Driver drives car, car does not drive driver....
class Driver {
    public:
        Driver(){
            std::cout << "A driver has entered" << std::endl;
        }
        ~Driver(){
            std::cout << "A driver has left" << std::endl;
        }
};

// Parent/base class 
class Car {
    public:
        Car(){
            std::cout << "A car is born" << std::endl;
        }
        ~Car(){
            std::cout << "The end of a car is here!" << std::endl;
        }
        std::string color = "";
        int maxSpeed = 0;
};

// Engine is a base class that is part of Honda 
class Engine {
    public:
    Engine(){
        std::cout << "I'm an engine hear me roar" << std::endl;
    }
    ~Engine(){
        std::cout << "The engine is tired now" << std::endl;
    }
};

// Inheritance is “IS-A” type of relationship
// Honda is and instance of Car (child/derived class)
class Honda : public Car{
    public:
        Honda(){
            std::cout << "A Honda is born" << std::endl;
        }
        ~Honda(){
            std::cout << "The end of a Honda is here!" << std::endl;
        }
        int totalSeats = 5;

        //Composition is a "part-of" relationship and the
        // class is dependant on the base class
        Engine myEngine; 
        Driver myDriver;
};


int main(){

    Honda myHonda;

    return 0;
}