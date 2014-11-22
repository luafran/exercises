class BinarySearchTree(object):
    def __init__(self):
        self._root = None

    def insert(self, key, value):
        if self._root:
            self._root.insert(key, value)
        else:
            self._root = BinarySearchTreeNode(key, value, True)

    def print_tree(self, indent):
        if self._root is None:
            print "Empty"
        else:
            self._root.print_tree(indent)


class BinarySearchTreeNode(object):
    def __init__(self, key, value, is_root=False):
        self.is_root = is_root
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def insert(self, key, value):
        if key < self.key:
            if self.left:
                self.left.insert(key, value)
            else:
                self.left = BinarySearchTreeNode(key, value)
        else:
            if self.right:
                self.right.insert(key, value)
            else:
                self.right = BinarySearchTreeNode(key, value)

    def print_tree(self, indent):
        if self.is_root:
            print "root"

        for i in range(indent):
            print " ",
        print "%s: %s" % (self.key, self.value)

        for i in range(indent):
            print " ",
        print "left"
        if self.left:
            self.left.print_tree(indent + 1)
        else:
            for i in range(indent + 1):
                print " ",
            print "None"

        for i in range(indent):
            print " ",
        print "right"
        if self.right:
            self.right.print_tree(indent + 1)
        else:
            for i in range(indent + 1):
                print " ",
            print "None"

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert('1', 1)
    tree.insert('2', 2)
    tree.insert('3', 3)
    tree.insert('4', 4)

    tree.print_tree(1)