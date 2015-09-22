from itertools import groupby

l = [
    {
        'name': 'product3',
        'price': 30,
        'category': 'cat1'
    },
    {
        'name': 'product2',
        'price': 10,
        'category': 'cat2'
    },
    {
        'name': 'product1',
        'price': 20,
        'category': 'cat2'
    },
    {
        'name': 'product5',
        'price': 40,
        'category': 'cat1'
    },
    {
        'name': 'product4',
        'price': 50,
        'category': 'cat3'
    }
]

s = sorted(l, key=lambda x: x['category'])
# print s

for key, group in groupby(s, lambda x: x['category']):
    print key
    for item in group:
        print item
    print " "
