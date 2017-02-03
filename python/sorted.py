from operator import itemgetter

alist = [
    {
        'name': 'product3',
        'price': 30
    },
    {
        'name': 'product2',
        'price': 10
    },
    {
        'name': 'product1',
        'price': 20
    }
]

s1 = sorted(alist)
print s1

s2 = sorted(alist, key=lambda item: item.get('price'))
print s2

s3 = sorted(alist, key=itemgetter('price'))
print s3
