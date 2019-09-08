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


def divide_by_base(dec_number):
    remstack = Stack()

    print(dec_number)
    while abs(dec_number) > 0:
        rem = dec_number % 2
        print('rem:', rem)
        remstack.push(rem)
        dec_number = dec_number // -2

    bin_string = ""
    while not remstack.is_empty():
        bin_string = bin_string + str(remstack.pop())

    return bin_string


x = 0
for i in range(len(A)):
    x = x + A[i] * pow((-2), i)

print(x)
print(divide_by_base(-x))
