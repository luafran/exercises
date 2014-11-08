# How to build a shared lib
CC=gcc
CFLAGS=-g

sources1=func1_v10.c func2_v10.c
OBJS1=$(sources1:.c=.o)

sources2=func1_v11.c func2_v11.c
OBJS2=$(sources2:.c=.o)

sources3=func1_v20.c func2_v20.c
OBJS3=$(sources3:.c=.o)

LIB_DIR=../lib
LIB_NAME=liblib1.so
LIB_NAME1=liblib1.so.1
LIB_NAME10=$(LIB_NAME1).0.0
LIB_NAME11=$(LIB_NAME1).1.0

LIB_NAME2=liblib1.so.2
LIB_NAME20=$(LIB_NAME2).0.0

all: $(LIB_NAME10) $(LIB_NAME11) $(LIB_NAME20)

$(LIB_NAME10): $(OBJS1)
	gcc -Wl,-soname,$(LIB_NAME1) -shared -fPIC -o $(LIB_NAME10) $^
	mv $(LIB_NAME10) $(LIB_DIR)
	ln -fs $(LIB_DIR)/$(LIB_NAME10) $(LIB_DIR)/$(LIB_NAME)

$(LIB_NAME11): $(OBJS2)
	gcc -Wl,-soname,$(LIB_NAME1) -shared -fPIC -o $(LIB_NAME11) $^
	mv $(LIB_NAME11) $(LIB_DIR)

$(LIB_NAME20): $(OBJS3)
	gcc -Wl,-soname,$(LIB_NAME2) -shared -fPIC -o $(LIB_NAME20) $^
	mv $(LIB_NAME20) $(LIB_DIR)

.c.o:
	$(CC) -c $(CFLAGS) $(INCPATH) -o "$@" "$<"

clean:
	rm *.o
