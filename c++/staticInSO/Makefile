
all: app1 app2


main1.o: main1.cpp
	g++ -c -pipe -g -fPIC $^

main2.o: main2.cpp
	g++ -c -pipe -g -fPIC $^

app1: main1.o
	g++ -Wl,-rpath,./lib -o $@ $^ -L./lib -ltest

app2: main2.o
	g++ -Wl,-rpath,./lib -o $@ $^ -L./lib -ltest

