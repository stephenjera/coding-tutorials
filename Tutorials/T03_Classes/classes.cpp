#include "classes.h"
#include <iostream>
using std::cout;

// Member function defintions
// Parameters can't have same name a private variables in class
void Vehicle::setModel(string m){
    model = m;
}

string Vehicle::getModel(){
    return model;
}

// Constructor definition 
Vehicle::Vehicle(string model){
    setModel(model);
}

// Destructor definition
Vehicle::~Vehicle(){
    cout << "Bye bye\n";
}


// Car virtual functions
void Car::move(){
    cout << "Move car\n";
}

// Truck virtual funtions
void Truck::move(){
    cout << "Move Truck\n";
}
