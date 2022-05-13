#pragma once
#include <string>
using std::string;

// Class declerations 
class Vehicle{
    public:
        // Constructor declration
        Vehicle(string);
        //destructor declrations
        ~Vehicle();

        // Member function declrations
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