#THE FIRST PART OF MANY

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names(a):
    for count in range(0, len(a)):
        print a[count]["first_name"], a[count]["last_name"]

#names(students)

################################################################################
#THE LAST PART OF MANY

users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

def weArewhoweAre(b):
    print "Students"
    # for count in range(0, len(b)):
    for num in range(0, len(b['Students'])):
        counter = 0
        print num + 1, "-", users['Students'][num]['first_name'], users['Students'][num]['last_name'], len(users['Students'][num]['first_name']) + len(users['Students'][num]['last_name'])

    print "Instructors"
    for num in range(0, len(b['Instructors'])):
        counter = 0
        print num + 1, "-", users['Instructors'][num]['first_name'], users['Instructors'][num]['last_name'], len(users['Instructors'][num]['first_name']) + len(users['Instructors'][num]['last_name'])

weArewhoweAre(users)


#the end of it all. this is it. no more. begone Hades, for my time has come.
