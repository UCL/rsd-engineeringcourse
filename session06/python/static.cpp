#include <iostream>
using namespace std;
class Counted{
    private:
            static int number_created;
    public:
                Counted(){
                            number_created++;
                                }
                    static int howMany(){
                                return number_created;
                                    }
};
int Counted::number_created=0;
int main(int argc,char **argv){
cout<< Counted::howMany() << endl;
Counted x=Counted();
cout<< Counted::howMany() << endl;
}
