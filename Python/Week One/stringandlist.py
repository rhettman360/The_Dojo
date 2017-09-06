#FIND AND REPLACE
words = "It's thanksgiving day. It's my birthday,too!"
old = "day"
new = "month"

#find "day"
print words.find(old)

#replace "day"
print words.replace(old, new)            #the assignment isn't exactly clear on whether or not it's every instance of the word day we have to replace, otherwise:
#print words.replace("day.", "month.")   This is it adjusted for just the first day

#######################################################################
#MIN AND MAX
x = [2,54,-2,7,12,98]

#find min
print min(x)

#find max
print max(x)

#######################################################################
#FIRST AND LAST
x = ["hello",2,54,-2,7,12,98,"world"]
first = None
last = None

#find first
first = x[0]

#find last
last = x[len(x)-1]

#create list
list = [first, last]
print list

#######################################################################
#NEW LIST
x = [19,2,54,-2,7,12,98,32,10,-3,6]
mid = None
new = []
temp = []

#sort list
x.sort()
print x

#find middle
mid = len(x) - (len(x)/2) - 1
print mid

#divide and conquer - first half
for count in range(0, mid):
    temp.append(x[count])
new.append(temp)

#divide and conquer - second half
counter = mid
for count in range (mid, len(x)):
    new.append(x[counter])
    counter += 1

#aaaaaaand print
print new

#end
