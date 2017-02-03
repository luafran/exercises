#include "Example.h"
#include "CollaboratorA.h"
#include "CollaboratorB.h"

struct ExampleImpl
{
    CollaboratorA m_a;
    CollaboratorB m_b;

    int getValue() { return m_a.getValue() + m_b.getValue(); }
};

Example::Example() : m_pImpl(new ExampleImpl)
{
}

Example::~Example()
{
    delete m_pImpl;
}

int Example::getValue()
{
    return m_pImpl->getValue();
}

int Example::getValue2()
{
    return m_pImpl->m_a.getValue() + m_pImpl->m_b.getValue();
}

