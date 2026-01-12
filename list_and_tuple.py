# marks = [96.8, 96.34, 97, 99, 92.10]

# print(marks)

thisList = ["apple", "banana", "cherry", "apple"]

# thisList.insert(0, "watermelon")

# thisList.append("watermelon")

# tropicalList = ["mango", "pineapple", "papaya"]
# thisList.extend(tropicalList)

# thisTuple = ("kiwi", "orange")
# thisList.extend(thisTuple)
# del thisList[-1]

# thisList.clear()

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newList = [x for x in fruits if "a" in x]

# print(newList)


# thisList = ["banana", "Orange", "Kiwi", "cherry"]

# thisList.sort(key = str.lower)

# print(thisList)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# list = ["hi", "i", "am", "shakib", "hi", "shakib"]

# list.insert(4, "ansari")
# print(list)

# student = ["Shakib", 18, 95.76]

# print(student)

# Strings are immutable but Lists are mutable

# String Immutability
# str = "Shakib"
# str = str.replace("a", "e")
# print(str)

# List Mutability

# list = ["ele1", "ele2", "ele3"]

# list[-1] = "elen"
# print(list)


# marks = [87, 64, 33, 95, 76];

# marks.append(89)
# print(marks)

# marks.sort(reverse=True)
# print(marks)


# intro = ["Hey", "Guys", "How", "Are", "You"]

# intro.sort()
# intro.reverse()
# print(intro)

# intro.insert(1, "Boys")

# print(intro)

# intro.remove("You");
# intro.pop(0)
# print(intro)


# Tuple


# tup = (87, 64, 33, 95, 76, 33)

# print(tup[-1])

# Write a program to ask the user to enter names of their 3 favorite movies & store them in a list.

# list = input("Enter the 3 Favorite Movies: ")
# print(list);


# movies = []

# movies.append(input("Enter first movie: "))
# movies.append(input("Enter second movie: "))
# movies.append(input("Enter third movie: "))

# print(movies)

# Write a program to check if a list contains a palindrome of elements.

# list = [1, "abc", "abc", 1]

# revList = list.copy()

# revList.reverse()

# print(list == revList)

# Write a program to cound the number of students with the "A" grade in the following tuple.

# tuple = ("C", "D", "A", "A", "B", "B", "A")

# print(tuple.count("A"))

# list = ["C", "D", "A", "A", "B", "B", "A"]

# list.sort()

# print(list)

# thisTuple = ("apple", "banana", "cherry", "apple", "banana")

# thisTuple[0] = "Apple"

# print(thisTuple)

# thisTuple = ("apple", True, 0, 1 )

# print(thisTuple[1] == thisTuple[3])

# print(type(thisTuple))


# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# thisList = list(thistuple)

# thisList.insert(0, "watermelon")


# thisTuple = tuple(thisList)

# print(thisTuple)

# Packing Tuple
# fruits = ("apple", "banana", "mango", "watermelon", "kiwi", "orange")

# print(fruits)

# Unpack the tuple

# (apple, banana, mango, *some_fruits) = fruits

# print("1. ", apple)
# print("2. ", banana)
# print("3. ", mango)
# print("4. ", some_fruits)


# thisTuple = ("shakib", "sameer", "sumit", "sourav")

# for i in range(len(thisTuple)): 
#     print(thisTuple[i])

# tup1 = (1, 2, 3, 4)
# tup2 = ("a", "b", "c", "d")

# tup3 = tup1 + tup2
# print(tup3)

# fruits = ("apple", "banana", "cherry")

# print(fruits * 2)

# tup1 = (1, 2, 3)
# tup2 = (4, 5, 6)

# print([tup1, tup2])

tup = ("a", "b", "c", "a", "a", "a", "c")

print(tup.index("c"))