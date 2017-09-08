class Product(object):
    """docstring for Product."""
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
        self.userInput()

    def used(self):
        print "This item is used but still in good condition. 20% off. Is this ok?"
        yn = raw_input("Y/N?> ")
        if yn == "yes" or yn == "y" or yn == "Yes" or yn == "Y":
            print "Awesome! Sold!"
            self.addTax()
            self.status = "Sold"
            self.cost = self.cost * .8
            print "Sold for: $", self.cost
            print "Your patronage is appreciated! Have a great day!"
        elif yn == "n" or yn == "no" or yn == "No" or yn == "N":
            print "We're sorry, have a great day!"
        else:
            print "Invalid input, try again"
            print ""
            self.used()

    def sell(self):
        print ""
        if self.status == "For Sale":
            self.addTax()
            self.status = "Sold"
            print "Sold for: $", self.cost
            print "Your patronage is appreciated! Have a great day!"
        elif self.status == "Sold":
            print "Sorry, we're sold out. Try again later!"
        elif self.status == "Defective":
            print "Sorry, this item was defective. Try again later!"
        elif self.status == "Used":
            self.used()
        else:
            print "Sorry, the item was", self.status
        self.userInput()

    def addTax(self):
        print ""
        self.cost = self.price
        completed = False
        while completed == False:
            tax = raw_input("Please enter tax rate: (round, no decimals)> ")
            if tax.isdigit():
                tax = float(tax)
                self.cost = self.cost * (tax/100 + 1)
                completed = True
                break
            else:
                print "Try again dumbass"
        return self.price

    def returnItem(self):
        print ""
        print "Please enter why you're returning this item"
        print ""
        print "If new in box, type used"
        print "If defective, please type defective"
        ret = raw_input(">")
        if ret == "used":
            self.status = "Used"
        elif ret == "defective":
            self.status = "Defective"
        else:
            self.status = "returned because", ret
        self.userInput()

    def displayInfo(self):
        self.addTax()
        print ""
        print "Item:", self.name
        print "Price: $", self.price
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Final Cost: $", self.cost
        print "Status: ", self.status
        self.userInput()

    def userInput(self):
        print ""
        print "Welcome! Please type in one of the following options!"
        opt = raw_input("info, buy, return, exit > ")
        if opt == "info":
            self.displayInfo()
        elif opt == "buy":
            self.sell()
        elif opt == "return":
            self.returnItem()
        elif opt == "exit":
            print ""
            print "Goodbye!!!"
            print ""
        else:
            print "Invalid command, please try again!"
            self.userInput()


Product(5, "Water", "1lb", "Fiji")



# var = raw_input("Please enter something: ")
# print "you entered", var
