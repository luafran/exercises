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


def is_balanced(sym_string):
    s = Stack()
    balanced = True
    index = 0

    while index < len(sym_string) and balanced:
        sym = sym_string[index]
        if sym.isspace():
            pass
        elif sym in '([{':
            s.push(sym)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, sym):
                    balanced = False
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(s1, s2):
    opens = "([{"
    closers = ")]}"
    return opens.index(s1) == closers.index(s2)


class TestBalancedSymbols(unittest.TestCase):

    def test_balanced(self):
        sym_string = ''
        self.assertTrue(is_balanced(sym_string))

        sym_string = '{{([][])}()}'
        self.assertTrue(is_balanced(sym_string))

        sym_string = '[[{{(( ))}}]]'
        self.assertTrue(is_balanced(sym_string))

        sym_string = '[][][]( )'
        self.assertTrue(is_balanced(sym_string))

        sym_string = '{}'
        self.assertTrue(is_balanced(sym_string))

    def test_not_balanced(self):
        sym_string = '('
        self.assertFalse(is_balanced(sym_string))

        sym_string = ']'
        self.assertFalse(is_balanced(sym_string))

        sym_string = '([ )]'
        self.assertFalse(is_balanced(sym_string))

        sym_string = '((( )]))'
        self.assertFalse(is_balanced(sym_string))

        sym_string = '[{( )]'
        self.assertFalse(is_balanced(sym_string))
