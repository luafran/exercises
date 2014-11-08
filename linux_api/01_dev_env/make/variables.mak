
# Uso de variables

PROG1_NAME=prog2
PROG1_OBJS=main1.o func1_v10.o func2_v10.o

$(PROG1_NAME): ${PROG1_OBJS}
	gcc -o $(PROG1_NAME) ${PROG1_OBJS}

main1.o: main1.c global.h
	gcc -c main1.c

func1_v10.o: lib1/func1_v10.c
	gcc -c lib1/func1_v10.c

func2_v10.o: lib1/func2_v10.c
	gcc -c lib1/func2_v10.c


clean:
	rm $(PROG1_NAME) ${PROG1_OBJS}
