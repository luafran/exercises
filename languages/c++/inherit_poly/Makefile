
all: inheritance

%.o: %.cxx
	g++ -c $?

inheritance: Base.o Derived.o main.o
	g++ -o $@ $^
