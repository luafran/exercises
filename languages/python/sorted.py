from operator import itemgetter

list = [
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

s1 = sorted(list)
print s1

s2 = sorted(list, key=lambda item: item.get('price'))
print s2

s3 = sorted(list, key=itemgetter('price'))
print s3
