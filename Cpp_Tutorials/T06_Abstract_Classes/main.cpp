#include <iostream>
using namespace std;

class Instrument
{
public:
     // Execute most derived implementation when using 
    // base class pointer (runtime polymorphism)
    // Virtual functions before regular functions
    virtual void makeMusic()
    {
        cout << "Virtual instrument playing\n";
    }

    void makeSound()
    {
        cout << "Instrument playing...\n";
    }
   
};

class Piano : public Instrument
{
public:
    // Regular function
    void makeSound()
    {
        cout << "A piano is playing...\n";
    }

    // Derived implementation of virtual function
    void makeMusic(){
        cout << "A virtual piano is playing...\n";
    } 
};

int main()
{
    // Regular class stuff
    Instrument instrument1;
    instrument1.makeSound();
    instrument1.makeMusic();

    // Pointer to base class
    Instrument *piano1 = new Piano;
    piano1->makeSound();
    piano1->makeMusic();

    // The brackets seemingly don't change anything
    Instrument *piano2 = new Piano();
    piano2->makeSound();
    piano2->makeMusic();
}
