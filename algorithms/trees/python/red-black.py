

class RedBlackTree(object):
    def __init__(self):
        self._tree = None

    def insert(self, n):
        if self._tree is None:
            self._tree = RedBlackTreeNode(n)
            self._tree.color = "Black"
        else:
            self._tree = self._tree.insert(n)

    def print_tree(self):
        if self._tree is None:
            print "Empty"
        else:
            self._tree.print_node(1)


class RedBlackTreeNode(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.color = "Red"
        self.parent = None

    def get_grand_parent(self):
        if self.parent is not None:
            return self.parent.parent
        else:
            return None

    def get_uncle(self):
        grand = self.get_grand_parent()
        if grand is not None:
            if grand.left == self.parent:
                return grand.right
            else:
                return grand.left
        else:
            return None

    def rebalance(self):
        # WP case 1: tree root
        if self.parent is None:
            self.color = "Black"
            return self
        # WP case 2: The parent of the target node is BLACK,
        # so the tree is in fine balance shape; just return the
        # tree root
        if self.parent.color == "Black":
            return self.get_root()
        # From here on, we know that parent is Red.
        # WP Case 3:  self, parent, and uncle are all red.
        if self.get_uncle() is not None and self.get_uncle().color == "Red":
            self.get_uncle().color = "Black"
            self.parent.color = "Black"
            self.get_grand_parent().color = "Red"
            return self.get_grand_parent().rebalance()
        # By now, we know that self and parent are red; and the uncle is black.
        # We also know that the grandparent is not None, because if it were, the
        # parent would be root, which must be black. So this means that we
        # need to do a pivot on the parent
        return self.pivot_and_rebalance()

    def get_root(self):
        if self.parent is None:
            return self
        else:
            return self.parent.get_root()

    def pivot_and_rebalance(self):
        # First, distinguish between the case where where my parent is
        # a left child or a right child.
        if self.get_grand_parent().left == self.parent:
            if self.parent.right == self:
                # WP case 4: I'm the right child of my parent, and my parent is the
                # left child of my grandparent. Pivot right around me.
                return self.pivot_left(False)
            else:
                # WP case 5
                # If I'm the left child, and my parent is the left child, then
                # pivot right around my parent.
                return self.parent.pivot_right(True)
        else:  # My parent is the right child.
            if self.parent.left == self:
                # WP case 4, reverse.
                return self.pivot_right(False)
            else:
                # WY case 5 reverse
                return self.parent.pivot_left(True)

    def pivot_right(self, recolor):
        # Hurrah, I'm going to be the new root of the subtree!
        # left = self.left
        right = self.right
        parent = self.parent
        grand = self.get_grand_parent()
        # move my right child to be the left of my soon-to-be former parent.
        parent.left = right
        if right is not None:
            right.parent = parent
        # Move up, and make my old parent my right child.
        self.parent = grand
        if grand is not None:
            if grand.right == parent:
                grand.right = self
            else:
                grand.left = self
        self.right = parent
        parent.parent = self
        if recolor is True:
            parent.color = "Red"
            self.color = "Black"
            return self.get_root()
        else:
            # re-balance from the new position of my former parent.
            return parent.rebalance()

    def pivot_left(self, recolor):
        # Hurrah, I'm going to be the new root of the subtree!
        left = self.left
        # right = self.right
        parent = self.parent
        grand = self.get_grand_parent()
        # move my left child to be the right of my soon-to-be former parent.
        parent.right = left
        if left is not None:
            left.parent = parent
        # Move up, and make my old parent my right child.
        self.parent = grand
        if grand is not None:
            if grand.right == parent:
                grand.right = self
            else:
                grand.left = self
        self.left = parent
        parent.parent = self
        if recolor is True:
            parent.color = "Red"
            self.color = "Black"
            return self.get_root()
        else:
            # re-balance from the position of my former parent.
            return parent.rebalance()

    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = RedBlackTreeNode(value)
                self.left.parent = self
                return self.left.rebalance()
            else:
                return self.left.insert(value)
        else:
            if self.right is None:
                self.right = RedBlackTreeNode(value)
                self.right.parent = self
                return self.right.rebalance()
            else:
                return self.right.insert(value)

    def print_node(self, indent):
        for i in range(indent):
            print "  ",
        print "%s (%s)" % (self.value, self.color)
        if self.left is None:
            for i in range(indent+1):
                print "  ",
            print "None(Black)"
        else:
            self.left.print_node(indent+1)
        if self.right is None:
            for i in range(indent+1):
                print "  ",
            print "None(Black)"
        else:
            self.right.print_node(indent+1)


if __name__ == '__main__':
    b = RedBlackTree()
    for i in range(10):
        b.insert(i)

    b.print_tree()
