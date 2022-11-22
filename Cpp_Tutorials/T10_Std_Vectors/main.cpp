#include <iostream>
#include <vector>
using std::vector;
using std::cout;


int main(){
    vector<int> myVector;

    // Append values to vector 
    for(int i; i < 10; i++){
        myVector.push_back(i);
        cout << i;
    }
    
    cout << "\n";

    // Print vector 
    for(auto i : myVector){
        cout << i;
    }
 
}