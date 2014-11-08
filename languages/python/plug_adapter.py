
class C1(object):
    def __init__(self):
        pass

    def __getattr__(self, name):
        def method(*args):
            print("tried to handle unknown method " + name)
            if args:
                print("    it had arguments: " + str(args))
        
        return method


c = C1()
c.foo()
c.bar("test", 1, True)

