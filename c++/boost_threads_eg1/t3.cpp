
#include <iostream>
#include <boost/thread.hpp>

class Worker
{
public:
    
    Worker(unsigned N, float guess, unsigned iter) 
            : m_Number(N),
              m_Guess(guess),
              m_Iterations(iter)
    {
        std::cout << "ctor" << std::endl;
    }

    Worker(const Worker &rhs)
            : m_Number(rhs.m_Number),
              m_Guess(rhs.m_Guess),
              m_Iterations(rhs.m_Iterations)
    {
        std::cout << "copy ctor" << std::endl;
    }

    void operator()()
    {
        std::cout << "Worker: calculating sqrt(" << m_Number
                  << "), itertations = " << m_Iterations << std::endl;

        // Use Newton's Method
        float   x;
        float   x_last = m_Guess;

        for (unsigned i=0; i < m_Iterations; i++)
        {
            x = x_last - (x_last*x_last-m_Number)/(2*x_last);
            x_last = x;

            std::cout << "Iter " << i << " = " << x << std::endl;
        }

        std::cout << "Worker: Answer = " << x << std::endl;
    }

private:

    unsigned    m_Number;
    float       m_Guess;
    unsigned    m_Iterations;
};

int main(int argc, char* argv[])
{
    std::cout << "main: startup" << std::endl;

    Worker w(612, 10, 5);
    boost::thread workerThread(w);
    //boost::thread workerThread(boost::ref(w));

    std::cout << "main: waiting for thread" << std::endl;

    workerThread.join();

    std::cout << "main: done" << std::endl;

    return 0;
}
