#include <iostream>

#include "Base.h"

using std::cout;
using std::endl;

Base::Base(void)
{
    //cout << "Base constructor (default)" << endl;
}

Base::Base(int i, int j): i(i), j(j)
{
    //cout << "Base constructor 2" << endl;
}

int Base::print(void)
{
    cout << "i = " << i << ", j = " << j << endl;
}

void Base::operator() (void)
{

    cout << "Base operator()" << endl;
}

