class Car(object):
    """docstring for Car."""
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.displayAll()

    def displayAll(self):
        self.taxAdjust()
        print str(self.price)
        print self.speed
        print self.fuel
        print self.mileage
        print self.tax

    def taxAdjust(self):
        if self.price > 10000:
            self.tax = "15%"
        else:
            self.tax = "12%"

test = Car(1000, "35mph", "Full", "15mpg")
test2 = Car(20000, "135mph", "Empty", "40mpg")
#end
