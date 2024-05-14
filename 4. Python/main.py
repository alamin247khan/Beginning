#String Methods
name = "i love my country"
print(len(name))
print(name.find("r"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("o","a"))
print(name*4)

#Type Casting = Convert the data type of a value to onather data type.
x = 1 #int
y = 2.0 #float
z = "3" #str
x = float(x)
y = int(y)
z = int(z)
z = str(z)
#print(x)
print("y is " + str(y))
print(z*3)


name = input("What is your name?: ")
age = int(input("who old are you?: "))
age = age + 1
height = input("what is your hight?: ")
print("My name is "+ name)
print("I am " + str(age) + " years old")
print("my height is "+ height)
