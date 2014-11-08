#ifndef _MSG2_H_
#define _MSG2_H_

#include "Msg.h"

class Msg2 : public Msg
{
public:
    
    Msg2();
    ~Msg2() {}
    virtual std::string getType() { return "Msg2"; }

private:
};

#endif

