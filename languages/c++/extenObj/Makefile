CXX_FLAGS += --coverage

all: extenObjDemo

main.o: main.cpp
		g++ --coverage -c $^

Msg.o: Msg.cpp
		g++ --coverage -c $^

Msg1.o: Msg1.cpp
		g++ --coverage -c $^

Msg2.o: Msg2.cpp
		g++ --coverage -c $^

Msg1ExtensionXMLSerializer.o: Msg1ExtensionXMLSerializer.cpp
		g++ --coverage -c $^

Msg2ExtensionXMLSerializer.o: Msg2ExtensionXMLSerializer.cpp
		g++ --coverage -c $^

extenObjDemo: main.o Msg.o Msg1.o Msg2.o Msg1ExtensionXMLSerializer.o Msg2ExtensionXMLSerializer.o
		g++ --coverage -o $@ $^ -lgcov

.PHONY: clean

clean:
		rm -rf extenObjDemo *.o *.gcov *.gcda *.gcno

