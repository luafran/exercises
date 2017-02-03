#ifndef _IMSGEXTENSIONXMLSERIALIZER_H_
#define _IMSGEXTENSIONXMLSERIALIZER_H_

#include "IMsgExtension.h"

class IMsgExtensionXMLSerializer : public IMsgExtension
{
public:
    virtual ~IMsgExtensionXMLSerializer() {}
    virtual std::string serialize() = 0;
};

#endif

