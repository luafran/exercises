#include <stdio.h>
#include <stdlib.h>

#define HASHSIZE 1024
#define MULTIPLIER 31

typedef struct Nameval Nameval;
struct Nameval
{
    char *name;
    int value;
    Nameval *next;
};

Nameval *hashtab[HASHSIZE];

void printNode(Nameval *p)
{
    printf("\np = %p\n", p);
    if (p != NULL)
    {
        printf("p->name = %s\n", p->name);
        printf("p->value = %d\n", p->value);
        printf("p->next = %p\n", p->next);
    }
}

unsigned int hash(char *name)
{
    unsigned int *c;
    unsigned int h;

    h = 0;
    for (c = (unsigned int *) name; *c != '\0'; c++)
        h = h * MULTIPLIER + *c;

    return h % HASHSIZE;
}

Nameval *lookup(char *name, int create, int value)
{
    int h;
    Nameval *sym;

    h = hash(name);
    for (sym = hashtab[h]; sym != NULL; sym = sym->next)
        if (strcmp(name, sym->name) == 0)
            return sym;

    if (create)
    {
        sym = malloc(sizeof(Nameval));
        sym->name = name;
        sym->value = value;
        sym->next = hashtab[h];
        hashtab[h] = sym;
    }
    
    return sym;
}

int main()
{
    Nameval *p;

    p = lookup("hello", 1, 10);
    printNode(p);
    p = lookup("bye", 1, 20);
    printNode(p);
    p = lookup("car", 1, 30);
    printNode(p);
    p = lookup("house", 1, 40);
    printNode(p);
    p = lookup("woman", 1, 50);
    printNode(p);
    p = lookup("child", 1, 60);
    printNode(p);
    
    p = lookup("house", 0, 40);
    printNode(p);
    
    p = lookup("notintable", 0, 60);
    printNode(p);

    return 0;
}

