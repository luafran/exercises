/* test.c */
#include <stdio.h>

unsigned int global_data = 33;
int global_data_2;

int main(int argc, char **argv)
{
    int local_data = 3;
    printf("Hello World\n");
    printf("global_data = %d\n", global_data);
    printf("global_data_2 = %d\n", global_data_2);
    printf("local_data = %d\n", local_data);
    return (0);
}

