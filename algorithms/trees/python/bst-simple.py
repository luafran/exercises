import unittest
from collections import deque


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.insert(value)

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


class TestTree(unittest.TestCase):

    def test_insert(self):

        # Tree from wikipedia
        # https://en.wikipedia.org/wiki/Tree_traversal
        
        tree = Node('F')

        tree.insert('B')
        tree.insert('A')
        tree.insert('D')
        tree.insert('C')
        tree.insert('E')

        tree.insert('G')
        tree.insert('I')
        tree.insert('H')

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

        def f(node):
            print node.value,

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
