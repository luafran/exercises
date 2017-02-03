#include <iostream>

class Base
{
public:
   virtual ~Base() { std::cout << "Base dtor\n"; }
   //~Base() { std::cout << "Base dtor\n"; }
   virtual void m1() = 0;
};


class D1 : public Base
{
public:
    virtual ~D1() { std::cout << "D1 dtor\n"; }
    virtual void m1() { std::cout << "inside d1\n"; }
};


int main()
{

   D1 d1;
   Base *bp = new D1();
   bp->m1();

    // If Base dtor is not virtual only Base dtor is called (D1 dtor is not called!)
   delete bp;
}

