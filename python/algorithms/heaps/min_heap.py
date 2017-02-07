import unittest
import heapq


class MinHeap:
    def __init__(self, a_list=None):
        if a_list is None:
            self.heap = [0]  # first element is not used
            self.size = 0
        else:
            self.build_heap(a_list)

    def build_heap(self, a_list):
        i = len(a_list) // 2  # don't have to process leaves
        self.size = len(a_list)
        self.heap = [0] + a_list[:]
        while i > 0:
            self._swap_down(i)
            i -= 1

    def insert(self, key):
        self.heap.append(key)
        self.size += 1
        self._swap_up(self.size)

    def extract_min(self):
        min_key = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self._swap_down(1)
        return min_key

    def min(self):
        return self.heap[1]

    def _swap_up(self, i):
        while i // 2 > 0:  # while node has a parent
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i //= 2  # go to parent

    def _swap_down(self, i):
        while (i * 2) <= self.size:  # while node has children
            min_child = self._min_child(i)
            if self.heap[i] > self.heap[min_child]:
                self.heap[min_child], self.heap[i] = self.heap[i], self.heap[min_child]
            i = min_child

    def _min_child(self, i):
        if i * 2 + 1 > self.size:  # node only has left child
            return i * 2
        else:
            if self.heap[i * 2] < self.heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def __str__(self):
        return 'heap: ' + str(self.heap) + ', size: {0}'. format(self.size)


class TestMinHeap(unittest.TestCase):

    def test_create_with_inserts(self):
        min_heap = MinHeap()
        min_heap.insert(10)
        min_heap.insert(5)
        min_heap.insert(15)
        min_heap.insert(17)
        print(min_heap)

        self.assertEqual(min_heap.size, 4)

        self.assertEqual(min_heap.extract_min(), 5)
        self.assertEqual(min_heap.size, 3)
        print(min_heap)

        self.assertEqual(min_heap.min(), 10)
        self.assertEqual(min_heap.size, 3)
        print(min_heap)

    def test_create_with_list(self):
        min_heap = MinHeap([10, 5, 15, 17])
        print(min_heap)

        self.assertEqual(min_heap.size, 4)

        self.assertEqual(min_heap.extract_min(), 5)
        self.assertEqual(min_heap.size, 3)
        print(min_heap)

        self.assertEqual(min_heap.min(), 10)
        self.assertEqual(min_heap.size, 3)
        print(min_heap)

        min_heap.insert(1)
        self.assertEqual(min_heap.min(), 1)
        self.assertEqual(min_heap.size, 4)
        print(min_heap)

    def test_python_heapq_min(self):
        min_heap = [10, 5, 15, 17]
        heapq.heapify(min_heap)
        print(min_heap)

        self.assertEqual(len(min_heap), 4)

        self.assertEqual(heapq.heappop(min_heap), 5)
        self.assertEqual(len(min_heap), 3)
        print(min_heap)

        self.assertEqual(min_heap[0], 10)
        self.assertEqual(len(min_heap), 3)
        print(min_heap)

        heapq.heappush(min_heap, 1)
        self.assertEqual(min_heap[0], 1)
        self.assertEqual(len(min_heap), 4)
        print(min_heap)

        heapq.he