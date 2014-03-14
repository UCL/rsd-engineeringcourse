#include <cassert>
#include <string>
using namespace std;

class MyClass {
    public:
    MyClass()
   : member("Value")
   {}
   string member;
};

int main(int argc, char **argv){
MyClass my_object = MyClass();
assert( my_object.member == "Value");
}
