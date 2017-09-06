list1 = ['magical unicorns',19,'hello',98.98,'world']
list2 = [2,3,1,7,4,12]
list3 = ['magical','unicorns']

def integerList(y):
    sum = 0
    for element in y:
        if isinstance(element, int):
            sum = sum + element
        if isinstance(element, float):
            sum = sum + element
    return sum

def stringList(x):
    newstr = "String: "
    for element in x:
        if isinstance(element, str):
            newstr += element + " "
    return newstr

def typeList(a):
    isint = False
    isstr = False
    isflt = False

    for element in a:
        # print "running"

        if isinstance(element, int):
            isint = True
            # print isint, "int"
        elif isinstance(element, float):
            isflt = True
            # print isflt, "flt"
        elif isinstance(element, str):
            isstr = True
            #print isstr, "str"

    if isint == True and isflt == False and isstr == False:     #integer
        print "The list you entered is of integer type"
        print "Sum:", integerList(a)

    elif isint == False and isflt == True and isstr == False:     #float
        print "The list you entered is of float type"
        print "Sum", integerList(a)

    elif isint == False and isflt == False and isstr == True:     #string
        print "The list you entered is of string theory"
        print stringList(a)

    else:
        print "The list you entered is of mixed type"
        print stringList(a)
        print "Sum:", integerList(a)

typeList(list1)
typeList(list2)
typeList(list3)
