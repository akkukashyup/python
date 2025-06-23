# dictionary

info = {
    "key" : "value",
    "name" : "akankha",
    "learning" : "coding",
    "age" : "7",
    "Is_adult" : "True",
    "subjects" : ["maths", "english", "hindi"],
    #list
    "topics" : ("dic","list","int",), 
    # tuples
    34.4 : 4566,
    #float
    756 : 5765
    #int
    }

print(info) 
print(type(info))   

print(info["subjects"])

# value change
info["name"] = "muskan"
print(info)

# new value pair add

info["surname"] = "kashyup"
print(info)

# empty dict

dic = {}

# add new value
dic["name"] = "rajat"

print(dic)