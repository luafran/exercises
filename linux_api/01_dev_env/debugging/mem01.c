#include <stdlib.h>

void f(void)
{
    int* x = malloc(10 * sizeof(int));
    // problem 1: heap block overrun
    // problem 2: memory leak -- x not freed
    x[10] = 0;
}                    

int main(void)
{
    f();

    return 0;
}

