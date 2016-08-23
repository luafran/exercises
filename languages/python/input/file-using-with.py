import sys

if len(sys.argv) < 2:
    print "usage:", sys.argv[0], "filename. - to read from stdin"
    raise SystemExit('Missing argument')

file_path = sys.argv[1]

with open(file_path, 'rb') as f:
    all_lines = f.readlines()
    print type(all_lines)
