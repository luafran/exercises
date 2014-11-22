import heapq


## {{{ http://code.activestate.com/recipes/577086/ (r1)
def heap_sort(u_list):
    def heapify(a):
        start = (len(a) - 2) / 2
        while start >= 0:
            shift_down(a, start, len(a) - 1)
            start -= 1

    def shift_down(a, start, end):
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

    heapify(u_list)
    end = len(u_list) - 1
    while end > 0:
        u_list[end], u_list[0] = u_list[0], u_list[end]
        shift_down(u_list, 0, end - 1)
        end -= 1


def heap_sort_2(u_list):
    heap = list(u_list)
    heapq.heapify(heap)
    for i in range(len(u_list)):
        u_list[i] = heapq.heappop(heap)

if __name__ == '__main__':
    list1 = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
    list2 = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
    heap_sort(list1)
    heap_sort_2(list2)
    print list1
    print list2
