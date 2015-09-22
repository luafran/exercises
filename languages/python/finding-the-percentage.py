n = input()
d = {}
for i in range(0,n):
    data = raw_input().split()
    d[data[0]] = data[1:]

student = raw_input()
marks = map(float, d[student])
average = reduce(lambda x,y: x+y, marks) / len(marks)
print "%.2f" % average
