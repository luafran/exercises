#include <stdio.h>

int dow(int y, int m, int d)
{
    static int t[] = {0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4};
    y -= m < 3;
    return (y + y/4 - y/100 + y/400 + t[m-1] + d) % 7;
}

int main(int argc, char* argv[])
{
    printf("1: Mon, 2: Tue, 3: Wed, 4: Thu, 5: Fri, 6: Sat, 7: Sun\n\n");
    printf("Today: dow(2016, 9, 6) = %d\n", dow(2016, 9, 6));
    printf("Luciano: dow(1976, 4, 27) = %d\n", dow(1976, 4, 27));
    printf("Alvaro: dow(2005, 9, 6) = %d\n", dow(2005, 9, 6));
    printf("Lorenzo: dow(2009, 8, 21) = %d\n", dow(2009, 8, 21));
    printf("Luciana: dow(1976, 8, 30) = %d\n", dow(1976, 8, 30));
    printf("Mama: dow(1945, 12, 5) = %d\n", dow(1945, 12, 5));
    printf("Flor: dow(1985, 9, 10) = %d\n", dow(1985, 9, 10));
}

