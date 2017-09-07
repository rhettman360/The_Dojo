class Hero(object):
    def __init__(self, name, city, powers):
        self.name = name
        self.city = city
        self.powers = powers

l1 = Hero("Luke Cage", "Harlem", ["Superhuman Strength", "Stamina"])

class Villain(object):
    def __init__(self, name, city, powers):
        self.name = name
        self.city = city
        self.powers = powers
    def displayinfo(self):
        print str(self.name)
joker = Villain("Joker", "New York City", "crazy")

class Sidekick(object):
    def __init__(self, name, city, powers):
        self.name = name
        self.city = city
        self.powers = powers

robin = Sidekick("Robin", "Gotham City", "gadget specialist")
