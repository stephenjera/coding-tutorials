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
    cout << test << endl;
    honda.move();
    lorry.move();

    return 0; 
}
