# creatin a list in python
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

# changing and accessing a list using the number position of the list
print(myFruitList[0])

print(myFruitList[1])

print(myFruitList[2])

myFruitList[2] = "orange"

print(myFruitList)
# creating a tuple which is immutable that means it can not be changed
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
# acessing the tuple by thier number position
print(myFinalAnswerTuple[0])

print(myFinalAnswerTuple[1])

print(myFinalAnswerTuple[2])

# creating a fruit dictionary
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}


print(myFavoriteFruitDictionary)

# to access individual's favourite fruit by thier name

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])


#creating a mixed-type list

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# using the for loop to print each item in the list
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))



