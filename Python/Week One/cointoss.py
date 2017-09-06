import random
def coinToss():
    head = 0
    tail = 0
    print "Starting the program..."
    for count in range(0, 5001):
        randomNum = random.random()
        if (randomNum >= 0.5):
            head = head + 1
            print "Attempt #", count, ": Throwing a coin... It's a head! ... Got", head, "head(s) so far and", tail, "tail(s) so far"
        else:
            tail = tail + 1
            print "Attempt #", count, ": Throwing a coin... It's a tail! ... Got", head, "head(s) so far and", tail, "tail(s) so far"


coinToss()
