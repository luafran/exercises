#ifndef _BASE_H_
#define _BASE_H_

class Base
{
    public:
        Base(void);
        Base(int i, int j);
        int print(void);
        virtual ~Base();

    private:
        int i, j;
};

#endif

