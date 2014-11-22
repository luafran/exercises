import sys
from random import randrange       


def qsort1a(u_list):
    """
    Quick sort using list comprehensions and randomized pivot
    """

    if u_list:
        print "list = %s" % u_list
        pivot = u_list.pop(randrange(len(u_list)))
        lesser = qsort1a([l for l in u_list if l < pivot])
        greater = qsort1a([l for l in u_list if l >= pivot])
        print "ret: %s %s %s" % (lesser, [pivot], greater)
        return lesser + [pivot] + greater
    else:
        print "list is empty"
        return []

if __name__ == "__main__":
    list_to_sort = map(int, sys.argv[1:])
    print "about to sort %s" % list_to_sort
    
    result = qsort1a(list_to_sort)
    print result
