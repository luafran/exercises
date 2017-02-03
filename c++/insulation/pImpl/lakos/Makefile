main: main.o Example.o CollaboratorA.o CollaboratorB.o
	g++ -o $@ $^

main.o: main.cpp Example.h

Example.o: Example.cpp Example.h CollaboratorA.h CollaboratorB.h

CollaboratorA.o: CollaboratorA.cpp CollaboratorA.h

CollaboratorB.o: CollaboratorB.cpp CollaboratorB.h

