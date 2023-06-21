#ifndef CLASSES_H
#define CLASSES_H
#include <string>
#include <iostream>
using std::string;

// Class declarations 
class Vehicle{
    public:
        // //destructor declaration
        ~Vehicle();

        // Member function declarations
        void setModel(string);
        string getModel();

        // pure virtual functions
        virtual void move() = 0;

     private:
        string model;
};

class Car : public Vehicle{
    public:
        Car(string);
        void move();
    private: 
        string model;
};

class Truck : public Vehicle{
    public:
        Truck(string);
        void move();
    private:
        string model;
};
#endif