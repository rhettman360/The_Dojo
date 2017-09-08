class FBTeam(object):
    def __init__(self, name, city, color):
        self.name = name
        self.city = city
        self.color = color
        self.players = []
    def __str__(self):
        return self.name + ", " + self.city + ", " + self.color + ", " + str(self.players)

class Player(object):
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number
    def __str__(self):
        return self.name + " " + self.position + " " + self.number

USC = FBTeam("Trojans", "LA", "Red, Yellow")
USC.players.append(Player("Reggie Bush", "Running Back", "5"))
USC.players.append(Player("Reggie Bush", "Running Back", "5"))
for player in USC.players:
    print player
print Player("Reggie Bush", "Running Back", "5")
print USC
