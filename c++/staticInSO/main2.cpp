#include <iostream>
#include "lib/LibClass.h"

int main()
{
    LibClass *lc = LibClass::getInstance();
    std::cout << "app2: lc = " << lc << std::endl;

    while(1)
    ;

    return 0;
}

