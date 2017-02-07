from collections import deque


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root:
            self._insert(key, value, self.root)
        else:
            self.root = BinarySearchTreeNode(key, value, True)

    def _insert(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left:
                self._insert(key, value, current_node.left)
            else:
                current_node.left = BinarySearchTreeNode(key, value)
        else:
            if current_node.right:
                self._insert(key, value, current_node.right)
            else:
                current_node.right = BinarySearchTreeNode(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left)
        else:
            return self._get(key, current_node.right)

    def apply_preorder(self, func):
        if self.root:
            self._apply_preorder(self.root, func)

    def _apply_preorder(self, current_node, func):
        if current_node is None:
            return
        func(current_node)
        self._apply_preorder(current_node.left, func)
        self._apply_preorder(current_node.right, func)

    def apply_inorder(self, func):
        if self.root:
            self._apply_inorder(self.root, func)

    def _apply_inorder(self, current_node, func):
        if current_node is None:
            return
        self._apply_inorder(current_node.left, func)
        func(current_node)
        self._apply_inorder(current_node.right, func)

    def apply_postorder(self, func):
        if self.root:
            self._apply_postorder(self.root, func)

    def _apply_postorder(self, current_node, func):
        if current_node is None:
            return
        self._apply_postorder(current_node.left, func)
        self._apply_postorder(current_node.right, func)
        func(current_node)

    def apply_levelorder(self, func):
        q = deque()
        q.appendleft(self.root)
        while len(q) > 0:
            node = q.pop()
            func(node)
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)

    def __getitem__(self, key):
        return self.get(key)

    def print_tree(self, indent):
        if self.root is None:
            print "Empty"
        else:
            self.root.print_tree(indent)


class BinarySearchTreeNode(object):
    def __init__(self, key, value, is_root=False):
        self.is_root = is_root
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def print_tree(self, indent):
        if self.is_root:
            print "root"

        for i in range(indent):
            print " ",
        print "%s: %s" % (self.key, self.value)

        for i in range(indent):
            print " ",
        # print "left"
        if self.left:
            self.left.print_tree(indent + 1)
        else:
            for i in range(indent + 1):
                print " ",
            print "None"

        for i in range(indent):
            print " ",
        # print "right"
        if self.right:
            self.right.print_tree(indent + 1)
        else:
            for i in range(indent + 1):
                print " ",
            print "None"

    def __iter__(self):
        if self:
            if self.left:
                for elem in self.left:
                    yield elem
            yield self.key
            if self.right:
                for elem in self.right:
                    yield elem


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert('F', '1')
    tree.insert('B', '2')
    tree.insert('G', '3')
    tree.insert('A', '4')
    tree.insert('D', '5')
    tree.insert('I', '6')
    tree.insert('C', '7')
    tree.insert('E', '8')
    tree.insert('H', '9')

    tree.print_tree(1)

    key = 'I'
    print('get({0})'.format(key))
    value = tree.get(key)
    print('value:', value)

    def f(node):
        print node.key,

    print('apply preorder')
    tree.apply_preorder(f)

    print()
    print('apply inorder')
    tree.apply_inorder(f)

    print()
    print('apply postorder')
    tree.apply_postorder(f)

    print()
    print('apply levelorder')
    tree.apply_levelorder(f)

    print()
    for n in tree.root:
        print(n)
