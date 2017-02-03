
class ClassA
{
public:
   explicit ClassA(int value): m_value(value) {}
   //ClassA(int value): m_value(value) {}
   ~ClassA() {}
private:
   int m_value;
};

void m1(const ClassA &a)
{
}

int main()
{
    // if explict is used in int ctor this is not allowed
    //ClassA c = 5;
    m1(ClassA(10));
}

