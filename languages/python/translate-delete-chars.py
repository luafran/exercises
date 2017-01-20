import string

in_str = '1123456789'
print 'in_str:', in_str

# Delete 1s and replace 2, 3, and 4 with x, y and z.
print in_str.translate(string.maketrans('234', 'xyz'), '1')
