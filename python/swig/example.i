%module example 
%{
#include "Class1.h"
%}

class Class1
{
public:
   Class1();
   ~Class1();

   void setY(int val);
   int getY();

   int x;

private:
   int y;
};

