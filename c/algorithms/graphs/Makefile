all: lib tests

tests: test_graph test_search


lib: graph.o search.o graph.h search.h
	gcc -shared -o libgraph.so -Wl,-soname=libgraph.so -Wl,--whole-archive graph.o search.o -Wl,--no-whole-archive

test_graph: lib test_graph.o
	gcc -o test_graph -Wl,-rpath=./ -Wl,--start-group test_graph.o -Wl,--end-group -L./ -lgraph

test_search: lib test_search.o
	gcc -o test_search -Wl,-rpath=./ -Wl,--start-group test_search.o -Wl,--end-group -L./ -lgraph
