class Bike(object):
    """docstring forBike."""
    def __init__(self, price, maxSpeed):
        self.price = price
        self.maxSpeed = maxSpeed
        self.miles = 0

    def displayInfo(self):
        return self.price, self.maxSpeed, str(self.miles)

    def ride(self):
        print "Riding"
        self.miles = self.miles + 10

    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles = self.miles - 5

def cx():
    cx500 = Bike("$1000", "120mph")
    for count in range(0,3):
        cx500.ride()
    cx500.reverse()
    print cx500.displayInfo()

def kz():
    kz1000 = Bike("$1500", "150mph")
    for count in range(0, 2):
        kz1000.ride()
    for count in range(0, 2):
        kz1000.reverse()
    print kz1000.displayInfo()

cx()
kz()
#end
