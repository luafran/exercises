import sys
from collections import defaultdict

if len(sys.argv) < 2:
    print "usage:",sys.argv[0],"filename"
    raise SystemExit

filename = sys.argv[1]

users = defaultdict(list)

f = open(filename)
#for line in open(filename):
for line in f:
    #print line,
    fields = line.split(':')
    user = fields[0].strip()
    uid = fields[2].strip()
    print 'user = {0}, uid = {1}'.format(user, uid)
    users[uid].append(user)

for k, v in users.iteritems():
    if len(v) > 1:
        print 'uid {0} has duplicated users {1}'.format(k, v)

