#include <iostream>

class Base
{
public:
   Base() {}
   ~Base() {}
   void m1()
   {
    std::cout << "m1 void in Base\n";
   }
   void m2(int a) {}
private:
   int m_value;
};

class Derived : public Base
{
public:
   Derived() {}
   ~Derived() {}

   // If we don't use this using directive m1() can not be used thru Derive instances
   // because we have another m1 with diff signature
   using Base::m1;
   void m1(int a)
   {
    std::cout << "m1 int in Derived\n";
   }
};

int main()
{
   Derived d;

   d.m1();
}

