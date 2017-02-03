import sys

if len(sys.argv) < 2:
    sys.stderr.write("usage: %s filename. - to read from stdin\n" % sys.argv[0])
    sys.exit(3)

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
