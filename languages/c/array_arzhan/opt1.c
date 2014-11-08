#include <stdio.h>
#include <stdlib.h>

#define SIZE 1024*1024*300

int main(void)
{
    int temp1, temp2;

    int *arr = (int *)malloc((SIZE)*sizeof(int));
    int i = SIZE;

    temp1 = clock();
    for (; i > 0; --i)
    {
        arr[i] = i;
    }
    temp2 = clock();

    printf("elapsed = %d\n", temp2-temp1);
}

