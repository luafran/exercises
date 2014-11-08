#include <iostream>
#include "Msg1.h"
#include "Msg1ExtensionXMLSerializer.h"

Msg1::Msg1()
{
    std::cout << "Msg1() this = " << this << std::endl;
    addExtension(std::string("XMLSerializer"), new Msg1ExtensionXMLSerializer(this));
}

