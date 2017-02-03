#include <iostream>

#include "Base.h"
#include "Derived.h"

using std::cout;
using std::endl;

Derived::Derived(void) : Base(8, 9)
{
    //cout << "Derived constructor" << endl;
}

void Derived::operator() (void)
{

    cout << "Derived operator()" << endl;
}

