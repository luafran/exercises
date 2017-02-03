#include <iostream>
#include <vector>

#include "Base.h"
#include "Derived.h"

using namespace std;

void f(Base* b);
void g(Base& b);

class Derived2 : public Base
{
    public:
        Derived2 () {};
        void operator() () { cout << "Derived2 operator()" << endl;};
};


int main(int argc, char* argv[])
{
    Base b;
    Derived2 d;

    vector<Base*> bp(2);

    b();
    d();

    bp[0] = new Base();
    bp[1] = new Derived2();

    f(bp[0]);
    f(bp[1]);
    

    return 0;
}


void f(Base* b)
{
    g(*b);
}

void g(Base& b)
{
    b();
}

