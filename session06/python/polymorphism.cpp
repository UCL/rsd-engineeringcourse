#include <string>
#include <iostream>
#include <vector>
using namespace std;

class Animal{
    public:
        virtual string noise()=0;
};

class Dog: public Animal {
    public:
    string noise(){
        return "Bark";
    }
};

class Cat: public Animal {
    public:
    string noise(){
        return "Miaow";
    }
};


int main(int argc, char**argv){
vector<Animal*> animals;
animals.push_back(new Dog());
animals.push_back(new Cat());
//animals.push_back(new Animal());
for(Animal* animal: animals) {
    cout << animal->noise() << endl;
}
}
