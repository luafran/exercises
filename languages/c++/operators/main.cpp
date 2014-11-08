#include <iostream>

using std::cout;
using std::endl;

class MyClass1
{
public:
    MyClass1() { cout << "default ctor\n"; }
    
    MyClass1(int i) : m_val(i)
    {
        cout << "int ctor\n";
    }
    
    MyClass1(const MyClass1& rhs) { cout << "copy ctor\n"; }
    
    ~MyClass1() { cout << "destructor\n"; }
    
    MyClass1& operator=(const MyClass1& rhs)
    {
        if (this == &rhs)
        {
            cout << "assignment to self\n";
            return *this;
        }

        cout << "copy assignment operator\n";
        return *this;
    }

    std::string to_str() const
    {
        return std::string("c1 as string");
    }
private:
    friend std::ostream& operator<<(std::ostream& os, const MyClass1& data);
    int m_val;

};

const MyClass1 operator*(const MyClass1& lhs, const MyClass1& rhs)
{
    cout << "operator*\n";

    return MyClass1();
}

std::ostream& operator<<(std::ostream& os, const MyClass1& data)
{
    // No need to be friend
    //return os << data.to_str() << " ";

    // excercise friendship
    return os << "val = " << data.m_val;
}

int main()
{

    MyClass1 c1;
    MyClass1 c2(c1);

    c2 = c1;

    c1 = c1;


    MyClass1 result;

    result = c1 * 2;
    result = 2 * c1;

    MyClass1 c3(27);
    cout << c3 << endl;
}
