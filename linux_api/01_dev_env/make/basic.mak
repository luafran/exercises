
# Basic Makefile

prog1: main1.o func1_v10.o func2_v10.o
	gcc -o prog1 main1.o func1_v10.o func2_v10.o

main1.o: main1.c lib1/lib.h
	gcc -c main1.c

func1_v10.o: lib1/func1_v10.c
	gcc -c lib1/func1_v10.c

func2_v10.o: lib1/func2_v10.c
	gcc -c lib1/func2_v10.c

clean:
	rm prog1 main1.o func1_v10.o func2_v10.o
