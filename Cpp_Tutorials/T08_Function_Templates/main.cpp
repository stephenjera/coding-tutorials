#include <iostream>

// create template function 
template <class T>
T sum(T x, T y){
    return x+y;
}

int main(){
    int a = 10;
    int b = 12;
    float c = 13.4;
    float d = 12.4556;

    // use function without defining types 
    std::cout << "a + b = " << sum(a,b) << std::endl;
    std::cout << "c + d = " << sum(c,d) << std::endl;
}