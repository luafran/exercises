#ifndef _MSG_H_
#define _MSG_H_

#include <string>
#include <map>
#include "IMsgExtension.h"

class Msg
{
public:
    
    Msg();
    ~Msg() {}

    virtual void addExtension(std::string id, IMsgExtension *extension);
    virtual IMsgExtension* getExtension(std::string id);
    virtual std::string getType() { return "Msg";}

private:
    std::map<std::string, IMsgExtension*> m_extensions;
};

#endif

