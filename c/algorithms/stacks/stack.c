/*
 *          File: stack.c
 *        Author: Robert I. Pitts <rip@cs.bu.edu>
 * Last Modified: March 7, 2000
 *         Topic: Stack - Array Implementation
 * ----------------------------------------------------------------
 *
 * This is an array implementation of a character stack.
 */

#include <stdio.h>
#include <stdlib.h>  /* for dynamic allocation */
#include <string.h>

/*
 * Type: stackElementT
 * -------------------
 * This is the type of the objects entered in the stack.
 * Edit it to change the type of things to be placed in
 * the stack.
 */

typedef char stackElementT;

/*
 * Type: stackT
 * --------------
 * This is the type for a stack, i.e., it is a type that
 * holds the information necessary to keep track of a stack.
 * It has a pointer `contents' to a dynamically-allocated
 * array (used to hold the contents of the stack), an integer
 * `maxSize' that holds the size of this array (i.e., the
 * maximum number of things that can be held in the stack),
 * and another integer `top,' which stores the array index of
 * the element at the top of the stack.
 */

typedef struct {
  stackElementT *contents;
  int maxSize;
  int top;
} stackT;

typedef stackT* stack_t;

/************************ Function Definitions **********************/

stack_t stack_new(int maxSize)
{

  stack_t new_stack = malloc(sizeof(stackT));

  stackElementT *newContents;

  /* Allocate a new array to hold the contents. */

  newContents = (stackElementT *) malloc(sizeof(stackElementT) * maxSize);

  if (newContents == NULL) {
    fprintf(stderr, "Insufficient memory to initialize stack.\n");
    exit(1);  /* Exit, returning error code. */
  }

  new_stack->contents = newContents;
  new_stack->maxSize = maxSize;
  new_stack->top = -1;  /* I.e., empty */

  return new_stack;
}

void stack_destroy(stack_t stack)
{
  /* Get rid of array. */
  free(stack->contents);

  stack->contents = NULL;
  stack->maxSize = 0;
  stack->top = -1;  /* I.e., empty */
}

void stack_push(stack_t stack, stackElementT element)
{
  if (stack_is_full(stack)) {
    fprintf(stderr, "Can't push element on stack: stack is full.\n");
    exit(1);  /* Exit, returning error code. */
  }

  /* Put information in array; update top. */

  stack->contents[++stack->top] = element;
}

stackElementT stack_pop(stack_t stack)
{
  if (stack_is_empty(stack)) {
    fprintf(stderr, "Can't pop element from stack: stack is empty.\n");
    exit(1);  /* Exit, returning error code. */
  }

  return stack->contents[stack->top--];
}

int stack_is_empty(stack_t stack)
{
  return stack->top < 0;
}

int stack_is_full(stack_t stack)
{
  return stack->top >= stack->maxSize - 1;
}

int main(void)
{
  stack_t stack;    /* A stack to hold characters. */
  char str[101];   /* String entered by user. */
  char *traverse;  /* Pointer used to traverse the string. */

  /*
   * Get a string from the user--don't enter more
   * than 100 characters!
   */
  printf("Enter a string: ");

  gets(str);  /* Read line, discard newline. */

  /*
   * Initialize the stack.  Make it at least
   * big enough to hold the string we read in.
   */
  stack = stack_new(strlen(str));
  /*
   * Traverse the string and put each
   * character on the stack.
   */

  for (traverse = str; *traverse != '\0'; traverse++) {
    stack_push(stack, *traverse);
  }

  /*
   * Pop each of the characters off of
   * the stack and print them out.
   */

  printf("\nPopped characters are: ");

  while (!stack_is_empty(stack)) {
    printf("%c", stack_pop(stack));
  }

  printf("\n");

  stack_destroy(stack);

  return 0;
}
