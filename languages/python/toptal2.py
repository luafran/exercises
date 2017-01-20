A = [1, 0, 0, 1, 1]


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


def divide_by_base(decNumber):
    remstack = Stack()

    print decNumber
    while abs(decNumber) > 0:
        rem = decNumber % 2
        print 'rem:', rem
        remstack.push(rem)
        decNumber = decNumber // -2

    binString = ""
    while not remstack.is_empty():
        binString = binString + str(remstack.pop())

    return binString


x = 0
for i in range(len(A)):
    x = x + A[i] * pow((-2), i)

print x
print divide_by_base(-x)
