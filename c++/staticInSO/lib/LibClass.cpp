
#include "LibClass.h"

LibClass::LibClass()
{
}

LibClass::~LibClass()
{
}

LibClass* LibClass::getInstance()
{
    static LibClass instance;
    return &instance;
}

