import heapq


# {{{ http://code.activestate.com/recipes/577086/ (r1)
def heap_sort(alist):
    def heapify(a):
        start = (len(a) - 2) / 2
        while start >= 0:
            sift_down(a, start, len(a) - 1)
            start -= 1

    def sift_down(a, start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and a[child] < a[child + 1]:
                child += 1
            if child <= end and a[root] < a[child]:
                a[root], a[child] = a[child], a[root]
                root = child
            else:
                return

    heapify(alist)
    end = len(alist) - 1
    while end > 0:
        alist[end], alist[0] = alist[0], alist[end]
        sift_down(alist, 0, end - 1)
        end -= 1


def heap_sort_2(alist):
    heap = list(alist)
    heapq.heapify(heap)
    for i in range(len(alist)):
        alist[i] = heapq.heappop(heap)

if __name__ == '__main__':
    list1 = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
    list2 = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
    heap_sort(list1)
    heap_sort_2(list2)
    print list1
    print list2
