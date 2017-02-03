import sys

if len(sys.argv) < 2:
    print 'usage: ...'
    raise SystemExit

file_name = sys.argv[1]

print file_name

f = open(file_name) 

fields = (line.split(':') for line in f)
for field in fields:
    print field
