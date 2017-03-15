import unittest


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


def list_search(head, item):
    current = head
    found = False
    while current is not None and not found:
        if current.item == item:
            found = True
        else:
            current = current.next

    return found


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
                if previous is None:
                    # found in head
                    self.head = current.next
                else:
                    # found in some other place
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


def has_cycle(head):
    seen = []

    cycle = False
    while head is not None:
        print('seen:', seen)
        print('head:', head)
        print('head.item', head.item)

        if head in seen:
            cycle = True
            break
        seen.append(head)
        head = head.next

    print('#' * 10)
    return cycle


def merge(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.head.item < list2.head.item:
        list1.head.next = merge(list1.head.next, list2.head)
        return list1
    else:
        list2.head.next = merge(list2.head.next, list1.head)
        return list2


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
            print(node.item)

    def test_contains(self):
        a_list = UnorderedList()
        a_list.add('item1')
        a_list.add('item2')
        a_list.add('item3')

        self.assertTrue('item3' in a_list)
        self.assertFalse('item4' in a_list)

    def test_has_cycle_false(self):
        node1 = Node('item1')
        self.assertFalse(has_cycle(node1))

        node2 = Node('item2')
        node1.next = node2

        self.assertFalse(has_cycle(node1))

    def test_has_cycle_true(self):
        node1 = Node('item1')
        node2 = Node('item2')
        node3 = Node('item3')
        node1.next = node2
        node2.next = node3
        node3.next = node2

        self.assertTrue(has_cycle(node1))

    def test_merge(self):
        a_list1 = UnorderedList()
        a_list1.add('item11')
        a_list1.add('item21')
        a_list1.add('item31')

        a_list2 = UnorderedList()
        a_list2.add('item12')
        a_list2.add('item22')
        a_list2.add('item32')

        head = merge(a_list1, a_list2)
        for node in head:
            print node.item
