from datetime import datetime, timedelta
import time


# Some utility classes / functions first
class AllMatch(set):
    """Universal set - match everything"""
    def __contains__(self, item): return True


allMatch = AllMatch()


def conv_to_set(obj):  # Allow single integer to be provided
    if isinstance(obj, (int,long)):
        return set([obj])  # Single item
    if not isinstance(obj, set):
        obj = set(obj)
    return obj


# The actual Event class
class Event(object):
    def __init__(self, action, min=allMatch, hour=allMatch, 
                       day=allMatch, month=allMatch, dow=allMatch, 
                       args=(), kwargs={}):
        self.mins = conv_to_set(min)
        self.hours= conv_to_set(hour)
        self.days = conv_to_set(day)
        self.months = conv_to_set(month)
        self.dow = conv_to_set(dow)
        self.action = action
        self.args = args
        self.kwargs = kwargs

    def matchtime(self, t):
        """Return True if this event should trigger at the specified datetime"""
        print "self.mins: {0}".format(self.mins)
        return ((t.minute     in self.mins) and
                (t.hour       in self.hours) and
                (t.day        in self.days) and
                (t.month      in self.months) and
                (t.weekday()  in self.dow))

    def check(self, t):
        if self.matchtime(t):
            self.action(*self.args, **self.kwargs)


class CronTab(object):
    def __init__(self, *events):
        self.events = events

    def run(self):
        t=datetime(*datetime.now().timetuple()[:5])
        while 1:
            print "{0} tick".format(time.strftime('%X'))
            print "minute: {0}, hour: {1}, day: {2}, month: {3}, weekday: {4}".format(t.minute, t.hour, t.day, t.month, t.weekday())
            for e in self.events:
                e.check(t)

            # t += timedelta(seconds=5)
            # while datetime.now() < t:
            #     time.sleep((t - datetime.now()).seconds)
            time.sleep(60)


def task1():
    print "{0} Executing task1".format(time.strftime('%X'))
    time.sleep(3)

def task2():
    print "{0} Executing task2".format(time.strftime('%X'))

def task3():
    print "{0} Executing task3".format(time.strftime('%X'))


c = CronTab(
    Event(task1),
    Event(task2, range(0,60,15)),
    Event(task3, range(0,60,3)),
)

c.run()
