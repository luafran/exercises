#ifndef _DERIVED_H_
#define _DERIVED_H_

#include "Base.h"

class Derived : public Base 
{
    public:
        Derived(void);
        virtual void operator() ();
};

#endif

