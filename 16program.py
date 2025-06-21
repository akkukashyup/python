# conditional statement

# else use only one time
# if and elif use many time

age = 14

if(age>=18):
    print("can vote")  #indentation{}  spaces
else:
    print("cannot vote")    


light = "green"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")

print("end the code")         



marks = int(input("enter student marks :"))

if(marks >= 90):
    grade ="A"
elif(marks >= 80 and marks < 90):
    grade ="B"
elif(marks >= 70 and marks < 80):
    grade ="C"
else:
    grade ="D"            

print("grade of the student -> ",grade)