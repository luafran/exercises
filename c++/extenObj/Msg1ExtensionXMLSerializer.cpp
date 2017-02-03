#include <iostream>
#include "Msg1.h"
#include "Msg1ExtensionXMLSerializer.h"

std::string Msg1ExtensionXMLSerializer::serialize()
{
   std::cout << "serialize() Serialize Msg1. m_msg = " << m_msg << std::endl;

    // just to show we have access to our message
    return m_msg->getType();
}

