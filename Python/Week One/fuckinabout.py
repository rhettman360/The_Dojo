obj = {"hello", "test"}

class Test(object):
    """docstring for Test."""
    def __init__(self, legs, color, material):
        self.legs= legs
        self.color = color
        self.material = material

    def printTest(self):
        print self.legs, self.color, self.material

chair = Test(5, "black", "pleather")
print chair.printTest()
