#MULTIPLES

#print odds from 1 to 1000
for count in range(1, 1000):
    if count % 2 != 0:
        print count

#print multiples of 5 from 5 to 1,000,000
for count in range(5, 1000000):
    if count % 5 == 0:
        print count

#######################################################################
#SUM LIST
a = [1, 2, 5, 10, 255, 3]
sum = 0

#loop through the list and add all the values
for element in a:
    sum = sum + element

#print dat sum
print sum

#######################################################################
#AVERAGE LIST
a = [1, 2, 5, 10, 255, 3]
sum = 0
avg = 0

#same as last time
for element in a:
    sum = sum + element

#find the average
avg = sum / len(a)

#and print it
print avg
