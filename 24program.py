# dictionary methods
# keys

student = {
    "name" : "rahul",
    "subject" : {
        "phy" : 7,
        "chem" : 9,
        "maths" : 10,
    }
}


# find keys

print(student.keys())

# change into list

print(list(student.keys()))

# find no of keys

print(len(student))
print(len(list(student.keys())))

