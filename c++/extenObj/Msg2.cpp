#include <iostream>
#include "Msg2.h"
#include "Msg2ExtensionXMLSerializer.h"

Msg2::Msg2()
{
    std::cout << "Msg2() this = " << this << std::endl;
    addExtension(std::string("XMLSerializer"), new Msg2ExtensionXMLSerializer(this));
}

