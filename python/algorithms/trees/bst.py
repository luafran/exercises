import unittest
from collections import deque


class BstNode:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BstNode(value, self)
            else:
                self.left.insert(value)
        elif value > self.value:
            if not self.right:
                self.right = BstNode(value, self)
            else:
                self.right.insert(value)
        else:
            raise ValueError('Duplicated key')

    def get(self, value):
        if value == self.value:
            return self
        elif value < self.value:
            if self.left:
                return self.left.get(value)
            else:
                return None
        else:
            if self.right:
                return self.right.get(value)
            else:
                return None

    def delete(self, value):

        # Incomplete!
        node_to_remove = self.get(value)

        if not (node_to_remove.left or node_to_remove.right):
            # is a leaf
            if node_to_remove == node_to_remove.parent.left:
                node_to_remove.parent.left = None
            else:
                node_to_remove.parent.right = None

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def find_max(self):
        current = self
        while current.right:
            current = current.right
        return current

    def contains(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left:
                return self.left.contains(value)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(value)
            else:
                return False

    def apply_preorder(self, f):

        f(self)
        if self.left:
            self.left.apply_preorder(f)
        if self.right:
            self.right.apply_preorder(f)

    def apply_preorder2(self, f):
        stack = []
        node = self
        while stack or node is not None:
            if node:
                f(node)
                if node.right:
                    stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()

    def apply_inorder(self, f):
        if self.left:
            self.left.apply_inorder(f)
        f(self)
        if self.right:
            self.right.apply_inorder(f)

    def apply_inorder2(self, f):
        stack = []
        node = self
        while stack or node is not None:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                f(node)
                node = node.right

    def apply_postorder(self, f):
        if self.left:
            self.left.apply_postorder(f)
        if self.right:
            self.right.apply_postorder(f)
        f(self)

    def apply_postorder2(self, f):
        stack = []
        last_visited = None
        node = self
        while stack or node is not None:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek_node = stack[len(stack)-1]
                if peek_node.right and last_visited is not peek_node.right:
                    node = peek_node.right
                else:
                    f(peek_node)
                    last_visited = stack.pop()

    def apply_levelorder(self, f):
        q = deque()
        q.appendleft(self)

        while len(q) > 0:
            node = q.pop()
            f(node)
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)

    def apply_levelorder2(self, f):

        order = []
        parent = {self.value: None}
        level = {self: 0}

        frontier = [self]

        next_level = 1
        while frontier:
            next_frontier = []
            for node in frontier:
                f(node)

                if node.left:
                    level[node.left.value] = next_level
                    parent[node.left.value] = node.value
                    next_frontier.append(node.left)

                if node.right:
                    level[node.right.value] = next_level
                    parent[node.right.value] = node.value
                    next_frontier.append(node.right)

            frontier = next_frontier
            next_level += 1

        print 'levels:', next_level-1
        print 'order:', order
        print 'parent:', parent
        print 'level:', level

    def __str__(self):
        return 'value: {0}, parent: {1}'.format(self.value, self.parent.value if self.parent else None)


def tree_clone(original_root):

    if not original_root:
        return None

    new_root = BstNode(original_root.value)
    clone = new_root

    while original_root:
        if original_root.left and not clone.left:
            clone.left = BstNode(original_root.left.value, clone)
            original_root = original_root.left
            clone = clone.left
        elif original_root.right and not clone.right:
            clone.right = BstNode(original_root.right.value, clone)
            original_root = original_root.right
            clone = clone.right
        else:
            original_root = original_root.parent
            clone = clone.parent

    return new_root


class TestTree(unittest.TestCase):

    def setUp(self):

        # Tree from wikipedia
        # https://en.wikipedia.org/wiki/Tree_traversal
        self.tree = BstNode('F')
        self.tree.insert('B')
        self.tree.insert('A')
        self.tree.insert('D')
        self.tree.insert('C')
        self.tree.insert('E')
        self.tree.insert('G')
        self.tree.insert('I')
        self.tree.insert('H')

    def test_insert(self):

        tree = self.tree
        self.assertTrue(tree.contains('A'))
        self.assertTrue(tree.contains('B'))
        self.assertTrue(tree.contains('C'))
        self.assertTrue(tree.contains('D'))
        self.assertTrue(tree.contains('E'))
        self.assertTrue(tree.contains('F'))
        self.assertTrue(tree.contains('G'))
        self.assertTrue(tree.contains('H'))
        self.assertTrue(tree.contains('I'))
        self.assertFalse(tree.contains('J'))

    def test_insert_duplicates(self):
        tree = BstNode('F')
        self.assertTrue(tree.contains('F'))
        self.assertRaises(ValueError, tree.insert, 'F')

    def test_get(self):

        node = self.tree.get('D')
        self.assertEqual(node.value, 'D')
        self.assertEqual(node.parent.value, 'B')
        self.assertEqual(node.left.value, 'C')
        self.assertEqual(node.right.value, 'E')

    def test_find_min(self):

        self.assertEqual(self.tree.find_min().value, 'A')

    def test_find_max(self):
        self.assertEqual(self.tree.find_max().value, 'I')

    def test_apply(self):

        tree = self.tree

        def f(node):
            print node

        print 'preorder'
        tree.apply_preorder(f)
        print
        tree.apply_preorder2(f)
        print
        print 'inorder'
        tree.apply_inorder(f)
        print
        tree.apply_inorder2(f)
        print
        print 'postorder'
        tree.apply_postorder(f)
        print
        tree.apply_postorder2(f)
        print
        print 'levelorder'
        tree.apply_levelorder(f)
        print
        tree.apply_levelorder2(f)

    def test_delete(self):
        tree = BstNode('F')
        tree.insert('B')
        tree.insert('A')
        tree.insert('D')
        tree.insert('C')
        tree.insert('E')
        tree.insert('G')
        tree.insert('I')
        tree.insert('H')

        # Node with no children
        self.assertTrue(tree.contains('H'))
        tree.delete('H')
        self.assertFalse(tree.contains('H'))

        # Node with one child
        self.assertTrue(tree.contains('G'))
        tree.delete('G')
        self.assertFalse(tree.contains('G'))

    def test_clone(self):
        print
        tree = self.tree
        tree2 = tree_clone(tree)

        def f(node):
            print node

        print 'original inorder'
        tree.apply_inorder(f)
        print 'cloned inorder'
        tree2.apply_inorder(f)
