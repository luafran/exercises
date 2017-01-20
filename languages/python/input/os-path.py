import os
import sys

if len(sys.argv) < 2:
    print "usage:", sys.argv[0], "filename"
    raise SystemExit('Missing argument')

file_name = sys.argv[1]

file_path = os.path.join(os.path.dirname(__file__), 'some-dir', file_name)

print 'File {0} exists?: {1}'.format(file_path, os.path.exists(file_path))

try:
    with open(file_path, 'r') as f:
        file_content = f.read()
        print 'type of file_content:', type(file_content)
        print file_content
except IOError as ex:
    print ex
