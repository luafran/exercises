#include <iostream>
#include "Msg1.h"
#include "Msg2.h"
#include "IMsgExtensionXMLSerializer.h"

void serializeMsg(Msg *m)
{
    std::string serMsg;

    IMsgExtensionXMLSerializer *e = dynamic_cast<IMsgExtensionXMLSerializer *>(m->getExtension("XMLSerializer"));
    if (e != NULL)
    {
        std::cout << "serializeMsg() e = " << e << std::endl;
        serMsg = e->serialize();
        std::cout << serMsg << std::endl;
    }    

    std::cout << std::endl;
}

int main()
{
    Msg *m1 = new Msg1();
    std::cout << std::endl;
    Msg *m2 = new Msg2();
    
    std::cout << "\n\n";
    serializeMsg(m1);
    serializeMsg(m2);

    return 0;
}

