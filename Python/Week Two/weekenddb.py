class DB(object):
    def __init__(self):
        self.contents = []
        self.next_id = 1
    def create(self,name):
        self.contents.append(User(name,self.next_id))
        self.next_id +=1
    def all(self):
        for element in self.contents:
            print element
    def get(self, id):
        for count in range(0, len(self.contents)):
            if self.contents[count].id == id:
                return self.contents[count]
    def filter(self, name):
        filterList = []
        for count in range(0, len(self.contents)):
            if self.contents[count].name == name:
                filterList.append(self.contents[count])
        for element in filterList:
            print "ID:{} Name:{}".format(element.id,element.name)
    def exclude(self, name):
        print self.contents[0].id
        exList =[]
        for count in range(0, len(self.contents)):
            if self.contents[count].name != name:
                exList.append(self.contents[count])
        for element in exList:
            print "ID:{} Name:{}".format(element.id,element.name)


class User(object):
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def __str__(self):
        return "Name: {}     ID: {}".format(self.name,self.id)


UserDB = DB()
UserDB.create("Mike")
UserDB.create("Rhett")
UserDB.create("Henry")
UserDB.exclude("Rhett")
UserDB.all()
