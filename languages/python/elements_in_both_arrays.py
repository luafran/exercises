a = map(int, raw_input().split())
b = map(int, raw_input().split())

set1 = set(a)
set2 = set(b)

for element in (set1 & set2):
    print element

