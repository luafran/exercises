#ifndef _MSG1_H_
#define _MSG1_H_

#include "Msg.h"

class Msg1 : public Msg
{
public:
    
    Msg1();
    ~Msg1() {}
    virtual std::string getType() { return "Msg1"; }

private:
};

#endif

