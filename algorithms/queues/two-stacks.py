import unittest


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def peek(self):
        self._refill_outbox_if_needed()
        return self.outbox.peek()

    def dequeue(self):
        self._refill_outbox_if_needed()
        return self.outbox.pop()

    def enqueue(self, item):
        self.inbox.push(item)

    def _refill_outbox_if_needed(self):
        if self.outbox.is_empty():
            while not self.inbox.is_empty():
                self.outbox.push(self.inbox.pop())


class TestQueue(unittest.TestCase):

    def test_peek(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual(1, q.peek())
        self.assertEqual(1, q.peek())

    def test_pop(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual(1, q.dequeue())
        self.assertEqual(2, q.dequeue())
        self.assertEqual(3, q.dequeue())
        self.assertTrue(q.outbox.is_empty())
        self.assertTrue(q.inbox.is_empty())

        q.enqueue(4)
        self.assertEqual(4, q.peek())
        self.assertEqual(4, q.dequeue())


if __name__ == '__main__':
    queue = Queue()
    t = int(raw_input())
    for line in xrange(t):
        values = map(int, raw_input().split())

        if values[0] == 1:
            queue.enqueue(values[1])
        elif values[0] == 2:
            queue.dequeue()
        else:
            print queue.peek()