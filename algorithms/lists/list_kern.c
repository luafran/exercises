#include <stdio.h>
#include <stdlib.h>

typedef struct Nameval Nameval;
struct Nameval
{
    char *name;
    int value;
    Nameval *next;
};


Nameval *newitem(char *name, int value)
{
    Nameval *newp;

    newp = (Nameval *) malloc(sizeof(Nameval));
    if (newp == NULL)
    {
        printf("newitem: cant allocate memory\n");
        exit(1);
    }

    newp->name = name;
    newp->value = value;
    newp->next = NULL;

    return newp;
}

Nameval *addfront(Nameval *listp, Nameval *newp)
{
    newp->next = listp;
    return newp;
}

Nameval *lookup(Nameval *listp, char *name)
{
    for (; listp != NULL; listp = listp->next)
        if (strcmp(name, listp->name) == 0)
            return listp;

    return NULL;
}


void apply(Nameval *listp, void (*fn)(Nameval*, void*), void *arg)
{
    for (; listp != NULL; listp = listp->next)
        (*fn)(listp, arg);
}

void printnv(Nameval *p, void *arg)
{
    char *fmt;

    fmt = (char *) arg;
    printf(fmt, p->name, p->value);
}

void freeall(Nameval *listp)
{
    Nameval *next;

    for (; listp != NULL; listp = next)
    {
        next = listp->next;
        free(listp);
    }
}

/* delitem: TODO: implement */

int main()
{
    Nameval *listp = NULL;

    listp = addfront(listp, newitem("hhhh", 2));
    listp = addfront(listp, newitem("oooo", 2));
    listp = addfront(listp, newitem("uuuu", 1));
    listp = addfront(listp, newitem("ssss", 4));
    listp = addfront(listp, newitem("eeee", 3));
    
    printf("apply\n");
    apply(listp, printnv, "%s: %d\n");
    
    return 0;
}

