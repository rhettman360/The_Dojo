class MathDojo(object):
    """docstring for MathDojo."""
    def __init__(self):
        self.sum = 0
        print "ran"

    def add(self, *args):
        self.adding = 0
        for count in range(0, len(args)):
            if isinstance(args[count], list) == True:
                for x in args[count]:
                    self.adding = self.adding + x
            else:
                self.adding  = self.adding + args[count]

        if self.add < 0:
            self.sum = self.sum - self.adding
        else:
            self.sum = self.sum + self.adding
        return self

    def subtract(self, *args):
        self.sub = args[0]
        for count in range(1, len(args)):
            if isinstance(args[count], list) == True:
                for x in args[count]:
                    self.sub = self.sub + x
            else:
                self.sub = self.sub + args[count]

        if self.sub < 0:
            self.sum = self.sum + self.sub
        else:
            self.sum = self.sum - self.sub
        return self

    def result(self):
        print self.sum
        self.sum = 0

md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).result()
