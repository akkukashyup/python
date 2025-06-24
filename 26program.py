# dic methods
# get

student = {
    "name" : "kumar",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "maths" : 99,
    }
}

print(student["name"])
print(student.get("name"))

# both are giving same value but same litle diffence

#print(student["name2"]) 
# error 

print(student.get("name2"))
# none value