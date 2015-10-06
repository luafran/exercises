from collections import deque

a = 'abbc'
b = 'bbccbbabc'

print 'a:', a
print 'b:', b
print

for i in range(0, len(b) - len(a) + 1):
    q = list(a)
    temp = b[i:i+len(a)]
    for c in temp:
        try:
            q.remove(c)
        except ValueError:
            pass
    print '{0} -> {1}'.format(temp, 'yes' if len(q) == 0 else 'no')
