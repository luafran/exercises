#include "Class1.h"
#include <iostream>

Class1::Class1()
{
   std::cout << "Class1 constructor\n";
}

Class1::~Class1()
{
   std::cout << "Class1 destructor\n";
}

void Class1::setY(int val)
{
   y = val;
}

int Class1::getY()
{
   return y;
}

