#include <stdio.h>
#include <stdlib.h>

typedef struct Nameval Nameval;
struct Nameval
{
    char *name;
    int value;
    Nameval *left;
    Nameval *right;
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
    newp->left = NULL;
    newp->right = NULL;

    return newp;
}

Nameval *insert(Nameval *treep, Nameval *newp)
{
    int cmp;

    if (treep == NULL)
        return newp;

    cmp = strcmp(newp->name, treep->name);
    if (cmp == 0)
    {
        printf("insert: duplicate entry %s ignored\n", newp->name);
    }
    else if (cmp < 0)
    {
        treep->left = insert(treep->left, newp);
    }
    else
    {
        treep->right = insert(treep->right, newp);
    }

    return treep;
}

Nameval *lookup(Nameval *treep, char *name)
{
    int cmp;

    if (treep == NULL)
        return NULL;

    cmp = strcmp(name, treep->name);
    if (cmp == 0)
        return treep;
    else if (cmp < 0)
        return lookup(treep->left, name);
    else
        return lookup(treep->right, name);
}

void applyinorder(Nameval *treep, void (*fn)(Nameval*, void*), void *arg)
{
    if (treep == NULL)
        return;

    applyinorder(treep->left, fn, arg);
    (*fn)(treep, arg);
    applyinorder(treep->right, fn, arg);
}

void applypostorder(Nameval *treep, void (*fn)(Nameval*, void*), void *arg)
{
    if (treep == NULL)
        return;

    applypostorder(treep->left, fn, arg);
    applypostorder(treep->right, fn, arg);
    (*fn)(treep, arg);
}

void printnv(Nameval *p, void *arg)
{
    char *fmt;

    fmt = (char *) arg;
    printf(fmt, p->name, p->value);
}

void printNode(Nameval *p, void *arg)
{
    char *title = (char *) arg;

    if (title != NULL)
        printf("\n%s\n", title);
    printf("p = %p\n", p);
    if (p != NULL)
    {
        printf("p->name = %s\n", p->name);
        printf("p->value = %d\n", p->value);
        printf("p->left = %p\n", p->left);
        printf("p->right = %p\n", p->right);
    }
}

int main()
{
    Nameval *treep = NULL;

    treep = insert(treep, newitem("hhhh", 2));
    treep = insert(treep, newitem("oooo", 2));
    treep = insert(treep, newitem("uuuu", 1));
    treep = insert(treep, newitem("ssss", 4));
    treep = insert(treep, newitem("eeee", 3));
    
    printf("applyinorder\n");
    applyinorder(treep, printNode, "applyinorder");
    printf("\napplypostorder\n");
    applypostorder(treep, printNode, "applypostorder");
    
    return 0;
}

