#ifndef _EXAMPLE_H_
#define _EXAMPLE_H_

class ExampleImpl;

class Example
{
private:
    ExampleImpl *m_pImpl;

public:
    Example();
    ~Example();

    int getValue();
    int getValue2();
};

#endif

