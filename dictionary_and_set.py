# dict = {
#     "name": "Shakib", 
#     "cgpa": 7.5, 
#     "marks": [78, 75, 78], 
#     "subjects": ["Python", "Java", "C++"], 
#     (12, 13, 14, 15): 12, 
# }

# print(dict)


# dict["name"] = "Sahib", 
# dict["surname"] = "Choudhry"

# print(dict)

# dict = {}

# dict["first_name"] = "Shakib"
# dict["last_name"] = "Ansari"
# dict["age"] = 18
# dict["marks"] = [87, 86, 89, 87, 69]
# dict["cgpa"] = 8.8

# print(dict)

# Nested Dictionary

# student = {
#     "name": "Shakib", 
#     "score": {
#         "chem": 98, 
#         "phy": 97, 
#         "math": 95
#     }
# }

# print(student["score"]["chem"])


# myDict = {
#     "first_name": "John", 
#     "last_name": "Wick", 
#     "age": 35, 
#     "net_worth": 89000000, 
#     "enemies": [
#         "Kutin", 
#         "Drumb", 
#         "Muti", 
#         "Jiyam"
#     ]
# }

# print(len(myDict))

# print(myDict.keys())
# print(myDict.items())
# print(myDict.get("age"))
# myDict.update({"flavour": "New Item", "age": 19})

# print(myDict.items())

# print(myDict)


# Sets

# collections = {9, True, False, 3, 4, 5,  10}

# print(len(collections))

# set = set()

# set.add(10)
# set.add(20)
# set.add(30)
# set.add(35)
# set.add(40)

# print(set.remove(10))
# print(set)

# set.add("Shakib")
# set.add("Ansari")
# set.add((1, 2, 3))

# print(set)

# set.clear()

# print(set)
# print(set.pop())


# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# print(set1.union(set2))
# print(set1.intersection(set2))

# Store following word meanings in a python dictionary: 

# dict = {
#     "table": ["a piece of furniture", "list of facts & figures"],
#     "cat": "a small animal"
#     }

# print(dict)

# subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}

# print(len(subjects))

# Write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

# marks = {}

# mark = int(input("Enter phy: "))
# marks.update({"phy": mark})

# mark = int(input("Enter chem: "))
# marks.update({"chem": mark})

# mark = int(input("Enter math: "))
# marks.update({"math": mark})

# print(marks)


# Set

# thisSet = {"apple", "banana", "guava", "apple", True, 1, 2}


# fruits = {"apple", "banana", "cherry", "grapes"}

# for fruit in fruits: 
#     print(fruit)


# removedItem = fruits.pop()

# print("Removed Item: ", removedItem)

# fruits = {"apple", "banana", "cherry", "grapes"}

# fruits.add("pineapple")

# print(fruits)

# fruits = {"apple", "banana", "cherry", "grapes"}

# tropicalFruits = {"mango", "pineapple", "papaya"}

# fruits.update(tropicalFruits)

# print(fruits)


# sets = {"this", "is", "just", "set"}

# sets.add("which")

# sets.discard("is")

# print(sets.pop())

# sets.clear()

# del sets

# print(sets)


# college_friends = {"sameer", "punit", "almaas", "zaid"}

# real_friends = {"sahal", "sahib", "arman", }

# all_friends = college_friends.union(real_friends)

# all_friends = college_friends.intersection(real_friends)

# all_friends = college_friends.difference(real_friends)

# all_friends = college_friends.symmetric_difference(real_friends)

# Equivalent to symmetric_difference -> ^

# all_friends = college_friends ^ real_friends
# print(all_friends)


# Dictionary

thisDict = {
    "name":"Shakib",
    "age": 19, 
    "roll_no": 30,
}

thisDict["city"] = "Delhi"


# print(len(thisDict))

# print(thisDict.get("roll_no"))

# print(thisDict.keys())

# thisDict['country'] = "India"
# print(thisDict)

# print(thisDict.keys())

# print(thisDict.values())

# thisDict['name'] = "Arman"

# print(thisDict.values())

# all = thisDict.items()
# print(all)

