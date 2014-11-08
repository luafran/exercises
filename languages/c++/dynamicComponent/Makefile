
all: main


#main: main.o component1.o component2.o
main: main.o component1.o component2.o component3.o
		g++ -o $@ $^

.PHONY: clean

clean:
		rm -rf main *.o

