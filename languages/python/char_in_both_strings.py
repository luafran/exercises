import sys

def chars_in_both_strings(string1, string2):

    for c in string1:
        if c in string2:
            print c

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "usage:",sys.argv[0],"string1 string2"
        raise SystemExit

    string1 = sys.argv[1]
    string2 = sys.argv[2]

    chars_in_both_strings(string1, string2)
else:
    print 'imported, __name__ =', __name__
