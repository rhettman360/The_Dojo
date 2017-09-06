l1 = [1,2,5,6,2]
l2 = [1,2,5,6,2]
l3 = [1,2,5,6,5]
l4 = [1,2,5,6,5,3]
l5 = [1,2,5,6,5,16]
l6 = [1,2,5,6,5]
l7 = ['celery','carrots','bread','milk']
l8 = ['celery','carrots','bread','milk']

def compareList(a, b):
    counter = 0
    if len(a) != len(b):
        return False
    for element in a:
        if element != b[counter]:
            return False
        counter = counter + 1
    return True

print compareList(l1, l2)
print compareList(l3, l4)
print compareList(l5, l6)
print compareList(l7, l8)
