#include <iostream>

class ClassA
{
public:
   ClassA(int value = 1) : m_value(value) {}
   ~ClassA() {}
   int getValue1() const { return m_value; }
   int getValue2() { return m_value; }
   void setValue(int value) const { m_value = value; }
private:
   mutable int m_value;
   //int m_value;
};

int main()
{
    const ClassA ca;

    std::cout << "value = " << ca.getValue1() << std::endl;
   
    // Not allowed if setValue is not const and m_value is not mutable
    ca.setValue(20);
   
    std::cout << "value = " << ca.getValue1() << std::endl;

    // not allowed since getValue2 is not const
    //std::cout << "value = " << ca.getValue2() << std::endl;

    // But allowed in non const objects
    ClassA a(5);
    std::cout << "value = " << a.getValue2() << std::endl;

}
