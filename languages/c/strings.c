#include <stdio.h>
#include <string.h>

size_t slen(char *s);
void scpy(char *s, char *t);
int scmp(char *s, char *t);

const int STR_MAX_SIZE = 10;

int main()
{
    char s1[] = "ABCDEFGHabcdefgh123456";
    char s2[] = "ABCDEFGHabcdefgh123456          ";
    char dest[100];
    char dest2[STR_MAX_SIZE+1];
    int i, j, c;

    memset(dest, 0, sizeof(dest));

    strcpy(dest, s1);
    strncpy(dest2, s1, STR_MAX_SIZE);
    dest2[STR_MAX_SIZE] = '\0';
    printf("dest2 = %s\n", dest2);

    printf("scmp(s1, dest) = %d\n", scmp(s1, dest));
    printf("scmp(s2, dest) = %d\n", scmp(s2, dest));
    
    printf("before reverse: \"%s\"\n", dest);

    for (i = 0, j = strlen(dest)-1; i < j; i++, j--)
    {
        c = dest[i];
        dest[i] = dest[j];
        dest[j] = c;
    }

    printf("after reverse: \"%s\"\n", dest);
    
    scpy(dest, s2);

    printf("before trim: \"%s\"\n", dest);

    for (i = strlen(dest)-1; i >= 0; i--)
    {
        if (dest[i] != ' ' && dest[i] != '\t' && dest[i] != '\n')
            break;
        dest[i] = '\0';
    }

    printf("after trim: \"%s\"\n", dest);

    printf("slen(s1) = %d\n", slen(s1));
}

size_t slen(char *s)
{
    size_t count = 0;
    for (;*s++ != '\0';count++)
        ;
    return count;
}

void scpy(char *s, char *t)
{
    while (*s++ = *t++)
        ;
}

int scmp(char *s, char *t)
{
    /*for (; *s == *t; s++, t++)*/
    while (*s++ == *t++)
        if (*s == '\0')
            return 0;
    
    return *s - *t;
}

