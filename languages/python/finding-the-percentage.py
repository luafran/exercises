# In Python 2 input() evaluates the string and raw_input() does not.
# In Python 3 there is only input() and is like Python 2 raw_input().
n = input()
d = {}
for i in range(0, n):
    data = raw_input().split()
    d[data[0]] = data[1:]

student = raw_input()
marks = map(float, d[student])
average = reduce(lambda x, y: x+y, marks) / len(marks)
print "%.2f" % average
