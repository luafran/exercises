stack = [3, 4, 5]
print stack
stack.append(6)
stack.append(7)
print stack
try:
    print stack.pop()
    print stack.pop()
    print stack.pop()
    print stack.pop()
    print stack.pop()
    print stack.pop()  # should throw
except Exception as e:
    print "Exception:", e.message
