// if a number is divisible by 3 output fizz, if divisible by 5 output buzz
// if divisible by both output Fizz Buzz

#include <iostream>
using std::cout;

int main(){
    for (int i = 1; i <= 100; ++i){
        bool flag;
        // Check if divisible by 5
        if(i % 5 == 0){
            // Set flag
            flag = true;
            // Check if divisible by 3
            if(i % 3 == 0){
                // Print Fizz Buzz
                std::cout <<"Fizz Buzz!!!\n";
                // Don't print the number 
                continue;
            } else if(flag){
                // Print Buzz
                std::cout << "Buzz\n";
                // Don't print the number
                continue;
            } else{
                // Number divisible by 5 but not 3
                // Print Fizz
                std::cout << "Fizz\n";
                // Don't print the number
                continue;
            }
        }
        // Print current number 
        std::cout << i << "\n";
    }

    return 0;
}