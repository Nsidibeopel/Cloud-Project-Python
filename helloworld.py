print("Hello, World")

print("Python has three numeric types: int, float, and complex")

myValue=1

print(myValue)

print(type(myValue))

print(str(myValue) + " is of the data type " + str(type(myValue)))


myValue=3.14

print(myValue)

print(type(myValue))


print(str(myValue) + " is of the data type " + str(type(myValue)))


myValue=5j

print(type(myValue))

print(str(myValue) + " is of the data type " + str(type(myValue)))


myValue=True

print(myValue)

print(type(myValue))


print(str(myValue) + " is of the data type " + str(type(myValue)))


myValue=False

print(str(myValue) + " is of the data type " + str(type(myValue)))



myString = "This is a string."
print(myString)

print(myString + " is of the data type " + str(type(myString)))

# Contetnation on python
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")

print(name)
# Input and feedback form on python
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))