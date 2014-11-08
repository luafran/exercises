def f1():
    print "f1"
    print __name__

if __name__ == "__main__":
    print repr(f1)
    s = "Test"
    print repr(s)
    l = ["one", "two", "three"]
    d = {"d1": "d1", "d2": "d2", "d3": "d3"}
    print "l = %s" % l
    #print "l = " + l doesnt work
    print "str(l) = " + str(l)
    print "repr(l) = " + repr(l)
