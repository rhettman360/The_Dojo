import random
randomNum = random.random() * 100
# print randomNum

def grades(a):
    if a <= 69 and a >= 60:
        print "Score:", a, ", Your grade is D"
    if a <= 79 and a >= 70:
        print "Score:", a, ", Your grade is C"
    if a <= 89 and a >= 80:
        print "Score:", a, ", Your grade is B"
    if a <= 100 and a >= 90:
        print "Score:", a, ", Your grade is A"
    else:
        print "Holy hell, you fail. Your score is", a
grades(randomNum)
grades(randomNum)
grades(randomNum)
grades(randomNum)
grades(randomNum)
grades(randomNum)
grades(randomNum)
grades(randomNum)
grades(randomNum)
grades(randomNum)
