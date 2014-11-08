import sys
from random import randrange       

def qsort1a(list):
    """
    Quicksort using list comprehensions and randomized pivot
    >>> qsort1a<<docstring test numeric input>>
    <<docstring test numeric output>>
    >>> qsort1a<<docstring test string input>>
    <<docstring test string output>>
    """
    if list == []:
        print "list is empty"
        return []
    else:
         print "list = %s" % list
         pivot = list.pop(randrange(len(list)))
         lesser = qsort1a([l for l in list if l < pivot])
         greater = qsort1a([l for l in list if l >= pivot])
         print "ret: %s %s %s" % (lesser, [pivot], greater)
         return lesser + [pivot] + greater

if __name__ == "__main__":
    listToSort = map(int, sys.argv[1:])
    print "about to sort %s" % listToSort
    
    result = qsort1a(listToSort)
    print result
