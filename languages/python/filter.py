from itertools import ifilter


l = [1, None, 3, None, 5, None, 7, None, 9, None]

# like [item for item in l if item]
l2 = filter(None, l)
print l2

# Like [item for item in l if function(item)]
l3 = filter(lambda x: x < 6, l)
print l3

# Returns an iterator, not a list
l4 = ifilter(lambda x: x < 6, l)
for item in l4:
    print item
