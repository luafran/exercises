from itertools import product

for i, j in product(range(3), repeat=2):
    print(i, j)

for i, j, k in product(['a', 'b', 'c'], repeat=3):
    print(i, j, k)
