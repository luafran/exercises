# How to build a static lib

sources=func3.c func4.c
OBJS=$(sources:.c=.o)
LIB_DIR=../lib

LIB_NAME=liblib2.a

all: $(OBJS)
	ar cqsv $(LIB_NAME) $?
	mv $(LIB_NAME) $(LIB_DIR)

.c.o:
	$(CC) -c $(CFLAGS) $(INCPATH) -o "$@" "$<"

