#include <iostream>
#include "Msg.h"

Msg::Msg()
{
}

void Msg::addExtension(std::string id, IMsgExtension *extension)
{
    std::cout << "addExtension() Adding extension: id = " << id << ", extension = " << extension << std::endl;
    m_extensions[id] = extension;
}

IMsgExtension* Msg::getExtension(std::string id)
{
    return m_extensions[id];
}

