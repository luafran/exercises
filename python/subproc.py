import subprocess as sp
import sys

file="/etc/passwd"
user="lafranll"

print "#" * 30,"check_output"
output = sp.check_output("cat " + file + " | grep " + user, shell=True).split(":")[2]
print "uid for", user, "is", output

print "#" * 30,"call"
try:
    retcode = sp.call("stat " + file, shell=True)
    if retcode < 0:
        print >>sys.stderr, "Child was terminated by signal", -retcode
    else:
        print >>sys.stderr, "Child returned", retcode
except OSError, e:
    print >>sys.stderr, "Execution failed:", e

print "#" * 30,"call unexisting command"
try:
    retcode = sp.call("mycmd" + " myarg", shell=True)
    if retcode < 0:
        print >>sys.stderr, "Child was terminated by signal", -retcode
    else:
        print >>sys.stderr, "Child returned", retcode
except OSError, e:
    print >>sys.stderr, "Execution failed:", e
