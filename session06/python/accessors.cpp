#include <string>
#include <iostream>
using namespace std;
class Person{
    private:
            string first;
            string second;

    public:
            Person():first("James"),second("Hetherington"){}
            string getName(){
                                return first + " " + second;
}};
int main(int argc, char**argv)
{
    Person p;
    cout << p.getName() << endl;
}
