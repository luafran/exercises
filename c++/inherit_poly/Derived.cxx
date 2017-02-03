#include <iostream>

#include "Base.h"
#include "Derived.h"

using std::cout;
using std::endl;

//Derived::Derived(void) : Base(8, 9)
Derived::Derived(void)
{
    cout << "Derived constructor" << endl;
}

