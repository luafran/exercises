
# Ejemplo de phony target con invocacion recursiva

CC=gcc
CFLAGS=-g -I./lib2

PROG1_NAME=prog4
sources1 = main2.c
OBJS1=$(sources1:.c=.o)
SUBDIRS = lib1 lib2
LIB_DIR=./lib

.PHONY: subdirs $(SUBDIRS)

$(PROG1_NAME): $(OBJS1) lib1
	gcc -g -o $@ $(OBJS1) -L$(LIB_DIR) -llib1 -llib2

.c.o:
	$(CC) -c $(CFLAGS) $(INCPATH) -o "$@" "$<"

lib1: lib2

subdirs: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@

include $(sources:.c=.d)

%.d: %.c
	$(CC) -MM $(CPPFLAGS) $< > $@.$$$$; \
	sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
	rm -f $@.$$$$
