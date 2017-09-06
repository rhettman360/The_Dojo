#PARTO UNO

x = [4,6,1,3,5,7,25]

def stars(a):
    for element in a:
        string = ""
        while element > 0:
            # print element
            element = element - 1
            string = string + "*"
        print string

stars(x)

################################################################################

#PARTO DOS

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def stars2(a):
    for element in a:
        if (isinstance(element, int)):
            string = ""
            while element > 0:
                # print element
                element = element - 1
                string = string + "*"
            print string
        elif (isinstance(element, str)):
            string2 = ""
            for count in element:
                string2 = string2 + element[0]
            print string2

stars2(x)
