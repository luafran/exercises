

class Subject(object):
    def __init__(self):
        self.observers = []

    def add_observer(self, obs):
        self.observers.append(obs)

    def do_something(self):
        for obs in self.observers:
            obs.notify()


class Observer1(object):
    def notify(self):
        print 'Observer1 - notify()'


class Observer2(object):
    def notify(self):
        print 'Observer2 - notify()'


def main():
    subject = Subject()
    observer1 = Observer1()
    observer2 = Observer2()
    subject.add_observer(observer1)
    subject.add_observer(observer2)
    subject.do_something()


if __name__ == '__main__':
    main()
