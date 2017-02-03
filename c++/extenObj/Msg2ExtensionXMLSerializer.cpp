#include <iostream>
#include "Msg2.h"
#include "Msg2ExtensionXMLSerializer.h"

std::string Msg2ExtensionXMLSerializer::serialize()
{
   std::cout << "serialize() Serialize Msg2. m_msg = " << m_msg << std::endl;

    // just to show we have access to our message
    return m_msg->getType();
}

