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


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist)-1)


def quick_sort_helper(alist, first, last):
    if first < last:

        split_point = partition(alist, first, last)

        quick_sort_helper(alist, first, split_point-1)
        quick_sort_helper(alist, split_point+1, last)


def partition(alist, first, last):
    pivot_value = alist[first]

    left_mark = first+1
    right_mark = last

    done = False
    while not done:

        while left_mark <= right_mark and alist[left_mark] <= pivot_value:
            left_mark += 1

        while alist[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            temp = alist[left_mark]
            alist[left_mark] = alist[right_mark]
            alist[right_mark] = temp

    temp = alist[first]
    alist[first] = alist[right_mark]
    alist[right_mark] = temp

    return right_mark


if __name__ == "__main__":
    list_to_sort = map(int, sys.argv[1:])
    print "about to sort %s" % list_to_sort
    
    #result = qsort1a(list_to_sort)
    #print result

    quick_sort(list_to_sort)
    print list_to_sort