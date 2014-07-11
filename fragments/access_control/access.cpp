class MyClass{
    public:
        void public_method(){
            private_method();
        }
    private:
        void private_method(){
        };
};
int main(int argc,char**argv){
    MyClass x=MyClass();
    x.public_method();
    //x.private_method();
}
