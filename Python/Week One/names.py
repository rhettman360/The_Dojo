students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names(a):
    for count in range(0, len(a)):
        print a[count]["first_name"], a[count]["last_name"]


names(students)
print students[1]["first_name"]
