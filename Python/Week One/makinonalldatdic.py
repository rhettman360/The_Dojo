name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favAnimal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def makinDict(a, b):
    newDict = {}
    newDict = zip(a,b)
    newDict = dict(newDict)
    return newDict

print makinDict(name, favAnimal)
