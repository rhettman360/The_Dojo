Num=1
while Num <= 100:
    Out=""
    if int(Num) % 3 == 0 and int(Num) % 5 == 0:
        Out+="FizzBuzz"
    elif int(Num) % 3 == 0:
        Out += "Fizz"
    elif int(Num) % 5 == 0:
        Out += "Buzz"
    else: Out += str(Num)

    print(Out)
    Num = Num + 1
