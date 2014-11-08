
all: libtest.so


LibClass.o: LibClass.cpp
	g++ -c -pipe -g -fPIC $^

libtest.so: LibClass.o
	g++ -shared -o $@ $^

