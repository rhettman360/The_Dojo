import random

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.qlength = len(self.calls)
        self.id = 1

    def add(self, name, pn, time, reason):
        self.calls.append(Call(name, pn, time, reason))

    def info(self):
        for element in self.calls:
            print "ID: {}  Name: {}  Phone # {}  Time: {}  Reason: {}".format(self.id,element.name,element.pn,element.time,element.reason)

class Call(object):
    def __init__(self, name, pn, time, reason):
        self.name = name
        self.pn = pn
        self.time = time
        self.reason = reason


    def display(self):
        print self.name
        print self.id
        print self.pn
        print self.time
        print self.reason



cc = CallCenter()
cc.add("Rhett", "425-244-0951", "12:00", "idk brah")
cc.add("Rhett", "425-244-0951", "12:00", "idk brah")
cc.info()
