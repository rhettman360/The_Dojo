class Animal(object):
    """docstring for Animal."""
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health = self.health - 1
        return self

    def run(self):
        self.health = self.health - 5
        return self

    def displayHealth(self):
        print self.health

class Dog(Animal):
    """docstring for Dog."""
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)

    def pet(self):
        self.health = self.health + 5

class Dragon(Animal):
    """docstring for Dragon."""
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)

    def fly(self):
        self.health = self.health - 10

    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon"


def ani():
    animal = Animal("Tank", 20)
    animal.walk()
    animal.walk()
    animal.walk()
    animal.run()
    animal.run()
    animal.displayHealth()

def doggo():
    doggo = Dog("Big ol' Pupper")
    doggo.walk()
    doggo.walk()
    doggo.walk()
    doggo.run()
    doggo.run()
    doggo.pet()
    doggo.displayHealth()

def bigSnake():
    lizard = Dragon("Snek")
    lizard.fly()
    lizard.displayHealth()

ani()
doggo()
bigSnake()
