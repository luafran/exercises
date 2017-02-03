#include <stdio.h>
#include <string.h>

int main()
{
    char *s1 = "cdefghijklmnopqrstuvwxy";
    char *s2 = "abxyz";

    char array[256];

    memset(array, 0, sizeof(array));

    for (; *s2 != '\0'; s2++)
        array[*s2] = 1;

    for (; *s1 != '\0'; s1++)
        if (array[*s1])
            printf("%c\n", *s1);
}
