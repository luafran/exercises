#include <iostream>

class Base
{
public:
   virtual ~Base() {}
   virtual void m1() = 0;
};


class D1 : public Base
{
public:
   virtual void m1() { std::cout << "inside d1\n"; }
};

class D2 : public Base
{
public:
   virtual void m1() { std::cout << "inside d2\n"; }
};


void process(Base &b)
{
   b.m1();
}

int main()
{

   D1 d1;
   D2 d2;

   process(d1);
   process(d2);

}

