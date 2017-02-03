#include <stdio.h>

static const unsigned char BitsSetTable256[256] = 
{
#   define B2(n) n,     n+1,     n+1,     n+2
#   define B4(n) B2(n), B2(n+1), B2(n+1), B2(n+2)
#   define B6(n) B4(n), B4(n+1), B4(n+1), B4(n+2)
    B6(0), B6(1), B6(1), B6(2)
};


int count1(unsigned int v)
{
    int c;
    // Option 1:
    c = BitsSetTable256[v & 0xff] + 
        BitsSetTable256[(v >> 8) & 0xff] + 
        BitsSetTable256[(v >> 16) & 0xff] + 
        BitsSetTable256[v >> 24]; 

    return c;
}


int count2(unsigned int v)
{
    int c;

    // Option 2:
    unsigned char * p = (unsigned char *) &v;
    c = BitsSetTable256[p[0]] + 
        BitsSetTable256[p[1]] + 
        BitsSetTable256[p[2]] + 
        BitsSetTable256[p[3]];

    return c;
}

/* K&R */
int count3(int v)
{
    int count;
    for (count=0; v; count++)
    {
        printf("v = 0x%x\n", v);
        printf("v-1 = 0x%x\n", v-1);
        v &= v-1;
        printf("v &= v-1 = 0x%x\n", v);
    }
    
    return count;
}

static const unsigned char BitsSetTable8[8] = 
{
    0, 1, 1, 2, 1, 2, 2, 3
};

int main()
{
    int i = 0;
    printf("count1(0xffffffff) = %d\n", count1(0xffffffff));
    printf("count2(0x0f0f0f0f) = %d\n", count2(0x0f0f0f0f));
    printf("count3(0x00000007) = %d\n", count3(0x00000007));
    printf("count3(0x0f000001) = %d\n", count3(0x0f000001));
    
    for (i = 0; i < 8; ++i)
    {
        printf("BitsSetTable8[%d] = %d\n", i, BitsSetTable8[i]);
    }

    printf("7 has %d 1s\n", BitsSetTable8[7]);
}

