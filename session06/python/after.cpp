#include <string>
using namespace std;



class Animal{
    public:
        int age;
    Animal(int age): age(age) {}
};

class Person: public Animal {
    public:
    string job;
    Person(int age, string job):Animal(age),job(job){}
};

class Pet: public Animal {
    public:
    Person & owner;
    Pet(int age, Person & owner):
        Animal(age), owner(owner)
    {}
};


int main(int argc, char **argv){
    Person me(37,"Programmer");
    Pet daisy(5,me);
}
