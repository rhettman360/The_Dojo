class Car():
    def __init__(self, color, wheels, brand):
        self.color = color
        self.wheels = wheels
        self.brand = brand
    def __str__(self):
        return self.color + 'This is the color'
myCar = Car('blue', 22, 'Fiat')
print myCar.color
print myCar
