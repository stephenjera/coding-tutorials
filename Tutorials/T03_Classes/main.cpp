#include <iostream>
#include "classes.h"
using std::cout;
using std::endl;

int main(){
    Car honda("Honda");
    Truck lorry("lorry");
    
    auto test = honda.getModel();
    cout << test << endl;
    test = lorry.getModel();
    honda.move();
    lorry.move();
    
}
