#include "classes.h"
#include <iostream>
using std::cout;

// Member function defintions
// Parameters can't have same name as private variables in class
void Vehicle::setModel(string m){
    model = m;
}

string Vehicle::getModel(){
    return model;
}

//Destructor definition
Vehicle::~Vehicle(){
    cout << "Bye bye\n";
}


// Car virtual functions
void Car::move(){
    cout << "Move car\n";
}

Car::Car(string model){
    setModel(model);
}

// Truck virtual functions
void Truck::move(){
    cout << "Move Truck\n";
}

Truck::Truck(string model){
    setModel(model);
}
