# dic method
# update

student = {
    "name" : "muskan",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "maths" : 99,
    }
}


student.update({"city" : "delhi" , "age" : 21})

# new = {"city" : "delhi" , "age" : 21}
# student.update(new)
####### its also work #####

student.update({"name":"akanksha"})

print(student)