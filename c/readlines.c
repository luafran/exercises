#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXLINE 1024

int mygetline(char *s, int lim);

int main()
{
    FILE *fp;
    char line[MAXLINE];
    int n = 0;

    fp = fopen("example.txt", "r");
    if (fp == NULL)
    {
        printf("Cant open file\n");
        exit(1);
    }

    printf("##### mygetline() #####\n");
    while ((n = mygetline(line, MAXLINE)) > 0)
    {
        line[n-1] = '\0';
        printf("%s\n", line);
    }

    printf("##### fgets() #####\n");
    while (fgets(line, MAXLINE, fp) != NULL)
    {
        line[strlen(line)-1] = '\0';
        printf("%s\n", line);
    }

    fclose(fp);
}

int mygetline(char *s, int lim)
{
    int c, i;

    i = 0;
    while(--lim > 0 && (c = getchar()) != EOF && c != '\n')
        s[i++] = c;

    if (c == '\n')
        s[i++] = c;

    s[i] = '\0';

    return i;
}

