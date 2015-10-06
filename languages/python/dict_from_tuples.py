import json
from collections import OrderedDict

tuples = [
    ('value1', 1, 'something1'),
    ('value2', 2, 'something2'),
    ('value3', 3, 'something3')
]

colnames = ('col1', 'col2', 'col3')

records = (dict(zip(colnames,t)) for t in tuples)
orecords = (OrderedDict(zip(colnames,t)) for t in tuples)

print 'dict:'
for record in records:
    print record

print
print 'ordered dict:'
for orecord in orecords:
    print json.dumps(orecord)

print
t = (1,2,3)
print zip(colnames,t)
print dict(zip(colnames,t))
