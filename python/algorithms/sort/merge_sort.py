import sys
import unittest


def merge_sort2(alist):

    print("Splitting ", alist)

    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1
    print("Merging ", alist)


def merge_sort(x):
    print('merge_sort: {0}'.format(x))
    if len(x) <= 1:
        return x

    # Recursive case. First, *divide* the list into equal-sized sublists.
    mid = len(x) // 2
    left_half = x[:mid]
    right_half = x[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # *Conquer*: merge the now-sorted sub lists.
    return merge(left_half, right_half)


def merge(left, right):
    print('merging: {0}, {1}'.format(left, right))
    result = list()
    # assign the element of the sublists to 'result' variable until there is no element to merge.
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            # compare the first two element, which is the small one, of each two sublists.
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]

    return result


class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.merge_sort = merge_sort

    def test_empty_list(self):
        print('#' * 20)
        self.assertEqual([], self.merge_sort([]))

    def test_one_element_list(self):
        print('#' * 20)
        self.assertEqual([3], self.merge_sort([3]))

    def test_two_element_list(self):
        print('#' * 20)
        self.assertEqual([20, 27], self.merge_sort([27, 20]))

    def test_several_elements_list_1(self):
        print('#' * 20)
        self.assertEqual([2, 5, 7, 11, 12, 13, 15, 20, 27, 30],
                         self.merge_sort([27, 20, 15, 12, 13, 11, 30, 5, 7, 2]))

if __name__ == "__main__":
    list_to_sort = map(int, sys.argv[1:])
    print "about to sort %s" % list_to_sort

    res = merge_sort(list_to_sort)
    print res

    # merge_sort2(list_to_sort)
    # print list_to_sort
