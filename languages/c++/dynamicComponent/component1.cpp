#include <iostream>

class Component1
{
public:
   static Component1* getInstance();
private:
   Component1() { std::cout << "Component1 constructor\n"; }
   ~Component1() {}
   
   static Component1 *m_instance;
};

Component1* Component1::getInstance()
{
   if (m_instance == 0)
   {
      m_instance = new Component1();
   }

   return  m_instance;
}

Component1 *Component1::m_instance = NULL;

Component1 *c1 = Component1::getInstance();

