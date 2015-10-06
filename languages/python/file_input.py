import sys

file_name = sys.argv[1]

try:
    with open(file_name) as f:
        for line in f:
            print line.rstrip('\n')
except IOError as ex:
    print 'exception:'
    print ex
