import sys

if len(sys.argv) < 2:
    print "usage:", sys.argv[0], "filename. - to read from stdin"

file_name = sys.argv[1]
if file_name == '-':
    f = sys.stdin
else:
    try:
        f = open(file_name)
    except IOError as ex:
        print 'exception:'
        print ex

# read all lines
# all_lines = f.readlines()

for line in f:
    print line.rstrip('\n')
