# nested dictionaries

student = {
    "name" : "rajat kumar",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "maths" : 99,
    }
}

print(student)

print(student["subject"])

print(student["subject"]["maths"])