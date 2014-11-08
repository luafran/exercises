import sys

#Import the ZSI client
from ZSI.client import Binding

u = 'http://127.0.0.1:8080'
n = ''
b = Binding(url=u, ns=n, host='127.0.0.1', port=8080)

#result = b.getMonth(2002, 2)
#print result[0]

result = b.getYear(2002)
print result[0]
