# '''
# if (condition):
#     code block 
# else:
#     code block for else

# '''

# if (1==2):
#     print("this is if condition")
#     a = 10
#     print(a)
# else:
#     print("this is else condition")


# a  = 13
# if (a%2==0):
#     print("this is even")

# else:
#     print("number is odd")

per = 80


# if(per>=80 and per<=100):
#     print("")

# elif(1==2):
#     print("this is elif code block")

# else:
#     print("this is false")

# print("hello")


# nested if 

'''
if(condition):
    if(condition):
        print("nested")
    else:
        print("nested else")
else:
    print("this is else")

'''






if (1==1):
    print("this is true")
    if(1==4):
        if (2>=2):
            print("this is true for nested nested ")
        else:
            print("this is nested nested else")
        print("nested if ")
    else:
        print("nested else condtion")
else:
    print("this is false")




gender = "Female"

if gender=="Female":
    print("Gender is female")
else:
    print("Gender is male")

# single line if condition or one line if 

result = "Gender is Female" if gender=="Male" else "Gender is male"
print(result)