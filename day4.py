# a = 10 => int 

# a = 4.3 => float

# a = "hello" ==> string


a = '1'
print("1" + "1")
print("1 "*3)

print(2+3j)

a = 10 
print("type check", type(a))

c = 2+3j
print("type check", type(c))

b = "hello"
print("type check", type(b))


a = "11"
b = "200"
print(a+b)

print(1+3.1)

#  manaul type casting

a = "11"
b = "200"
print("before type casting", a+b)
# print(a+b)


print("after type casting",int(a)+int(b))


a = "hello"
# print(int(a))


a = True

print(type(a))


a = False

print(type(a))

a = "22"
print(isinstance(a, str))

b = 11
print(isinstance(b, int))


test = "hello"
test2 = "from broadway"
test3 = 2222
test4 = 2222


# hello from broadway 4444

print(test, test2, test3)
print(test+ "   " +test2 + "      " +str(test3))


# string formatting  f''


print(f'{test} {test2}  {test3+test4}')
print(f"{test}   !   {test3}")



# python string
test = "heLLo sudan"
print(test.upper())
print(test.lower())
print(test.title())
print(test.capitalize())
print(test.count("L"))