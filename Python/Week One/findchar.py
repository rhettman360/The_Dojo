words = ['hello','world','my','name','is','Anna']
char = 'o'
newstr = []
word = None

for element in words:
    # print element
    word = element
    for letter in element:
        # print letter
        if letter == char:
            newstr += word
print newstr
