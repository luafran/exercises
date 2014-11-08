#ifndef _MSG2EXTENSIONXMLSERIALIZER_H_
#define _MSG2EXTENSIONXMLSERIALIZER_H_

#include "IMsgExtensionXMLSerializer.h"

class Msg2;

class Msg2ExtensionXMLSerializer : public IMsgExtensionXMLSerializer
{
public:

    Msg2ExtensionXMLSerializer(Msg2 *m) : m_msg(m) {}
    ~Msg2ExtensionXMLSerializer() {}

    std::string serialize();

private:    
    Msg2 *m_msg;

};

#endif

