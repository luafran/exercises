#include <iostream>

class Component2
{
public:
   Component2() { std::cout << "Component2 constructor\n"; }
   ~Component2() {}
private:
};

Component2 *c2 = new Component2();

