#include <string>
using namespace std;

class Person{
    public:
    int age;
    string job;
    Person(int age, string job): 
        age(age), job(job)
        {}
};

class Pet{
    int age;
    Person & owner;
    Pet(int age, Person & owner):
        age(age), owner(owner)
        {}
};

int main(int argc, char **argv){
    Person me(37,"Programmer");
}
