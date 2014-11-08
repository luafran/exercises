# Ejemplo de reglas implicitas
#CC=gcc
#CFLAGS += -g
LDFLAGS = -fPIC

PROG1_NAME=prog3
PROG1_OBJS=main1.o lib1/func1_v10.o lib1/func2_v10.o

$(PROG1_NAME): ${PROG1_OBJS}
	gcc -o $(PROG1_NAME) ${PROG1_OBJS}

main.o: global.h


.PHONY: clean

clean:
	rm $(PROG1_NAME) ${PROG1_OBJS}
