import random
from random import shuffle

class Cards(object):
    """docstring for Cards."""

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value


def createDeck():
    deck = []
    for suit in range(14,18):
        # print suit
        suitVal = [suit]
        for card in range(1,14):
            # print card
            cardVal = [card]
            deck.append([suitVal, cardVal])
    return deck

def intepretDeck(a):
    wordDeck = []
    for element in a:
        # print element[0]

        if element[0] == [14]:
            wordDeck.append("Hearts")
        elif element[0] == [15]:
            wordDeck.append("Spades")
        elif element[0] == [16]:
            wordDeck.append("Diamonds")
        elif element[0] == [17]:
            wordDeck.append("Clubs")

        if element[1] == [1]:
            wordDeck.append("Ace")
            #print 'test'
        elif element[1] == [11]:
            wordDeck.append("Jack")
        elif element[1] == [12]:
            wordDeck.append("Queen")
        elif element[1] == [13]:
            wordDeck.append("King")
        else:
            wordDeck.append(element[1][0])
    return wordDeck

def condenseDeck(b):
    condDeck = []
    for pair in range (0, len(b)):
        if (pair % 2 == 0):
            piece = []
            # print b[pair]
            piece.append(b[pair])
            piece.append(b[pair+1])
            condDeck.append(piece)
    shuffle(condDeck)
    return condDeck

# def drawCard(c):
#     print "You drew the", c[0][1], "of", c[0][0] + ","
#     print "The", c[1][1], "of", c[1][0] + ","
#     print "The", c[2][1], "of", c[2][0] + ","
#     print "The", c[3][1], "of", c[3][0] + ","
#     print "The", c[4][1], "of", c[4][0] + ","
#     print "he", c[5][1], "of", c[5][0] + ","
#     print "and the", c[6][1], "of", c[6][0] + "."

x = condenseDeck(intepretDeck(createDeck()))
hand = Cards(x[0][0], x[0][1])

print hand.suit, "of", hand.value




#end
