#ifndef _MSG1EXTENSIONXMLSERIALIZER_H_
#define _MSG1EXTENSIONXMLSERIALIZER_H_

#include "IMsgExtensionXMLSerializer.h"

class Msg1;

class Msg1ExtensionXMLSerializer : public IMsgExtensionXMLSerializer
{
public:

    Msg1ExtensionXMLSerializer(Msg1 *m) : m_msg(m) {}
    ~Msg1ExtensionXMLSerializer() {}

    std::string serialize();

private:    
    Msg1 *m_msg;

};

#endif

