#ODD/EVEN

def oddEven():
    for count in range(1, 2001):
        if(count % 2 == 0):
            print "Number is", count, ". This is an even number."
        if(count % 2 != 0):
            print "Number is", count, ". This is an odd number."
# oddEven()
################################################################################

#MULTIPLY

a = [2,4,10,16]

def multiply(x, b):
    for count in range(0, len(x)):
        # print count
        x[count] = x[count] * b
    print x

# multiply(a, 5)
################################################################################

arr = [2,4,5]
newarr = []

def layeredMultiples(y):
    for element in y:
        mul = []
        while element > 0:
            print element
            element = element - 1
            mul.append(1)
            print mul
        newarr.append(mul)
    print newarr

layeredMultiples(arr)
