import unittest


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class UnorderedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
        self.size += 1

    def remove(self, item):

        current = self.head
        previous = None

        while current is not None:
            if current.item == item:
                # found
                # in head
                if previous is None:
                    self.head = current.next
                # in some other place
                else:
                    previous.next = current.next

                self.size -= 1
                break

            previous = current
            current = current.next

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.item == item:
                found = True
            else:
                current = current.next

        return found

    def __iter__(self):
        current = self.head

        while current is not None:
            yield current
            current = current.next

    def __contains__(self, item):
        return self.search(item)


class TestUnorderedList(unittest.TestCase):

    def test_add_and_search(self):
        a_list = UnorderedList()
        self.assertEqual(0, a_list.size)

        a_list.add('item1')
        a_list.add('item2')
        a_list.add('item3')

        self.assertEqual(3, a_list.size)
        self.assertTrue(a_list.search('item2'))
        self.assertFalse(a_list.search('item4'))

    def test_remove(self):
        a_list = UnorderedList()
        self.assertEqual(0, a_list.size)

        a_list.remove('something')
        self.assertEqual(0, a_list.size)

        a_list.add('item1')
        a_list.add('item2')
        a_list.add('item3')
        self.assertEqual(3, a_list.size)
        self.assertTrue(a_list.search('item3'))

        a_list.remove('item3')

        self.assertEqual(2, a_list.size)
        self.assertFalse(a_list.search('item3'))

        a_list.remove('unexisting')
        self.assertEqual(2, a_list.size)

    def test_iter(self):
        a_list = UnorderedList()
        a_list.add('item1')
        a_list.add('item2')
        a_list.add('item3')

        for node in a_list:
            print node.item

    def test_contains(self):
        a_list = UnorderedList()
        a_list.add('item1')
        a_list.add('item2')
        a_list.add('item3')

        self.assertTrue('item3' in a_list)
        self.assertFalse('item4' in a_list)
