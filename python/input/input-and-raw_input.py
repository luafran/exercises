# In Python 2 input() evaluates the string and raw_input() does not.
# In Python 3 there is only input() and is like Python 2 raw_input().
i1 = input('please enter an int (using input): ')
i2 = raw_input('please enter an int (using raw_input): ')
print 'type(i1):', type(i1), 'val:', i1
print 'type(i2):', type(i2), 'val:', i2
i3 = map(int, raw_input('please enter a list of ints separated by space: ').split())
print 'type(i3):', type(i3)
print 'i3:', i3
