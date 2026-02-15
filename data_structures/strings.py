# str1 = 'This is string 1'
# str2 = "This is string 2"
# str3 = """This is string 3"""
# str4 = '''This is string 4'''

# print(type(str1))
# print(type(str2))
# print(type(str3))
# print(type(str4))

# str5 = "this is shakib ansari's program"
# print(str5)

# str1 = "This is end.\nPlease learn from here"
# print(str1)

# String Concatenation

# str1 = "Shakib"
# str2 = "Ansari"

# print(str1+" "+str2)

# print(len(str2))

# str1[1] = "G"

# print(str1[1])


# String Slicing


# str1 = "Hey, I am Shakib Ansari, Founder and CEO";

# owner = str1[10: 23];
# print("This is Owner: ", owner)


# str1 = input("Enter your name: ")

# # shakib

# print(str1[ -4: -1])


# String Functions

# str = "shakib ansari"

# print(str.endswith("sari"))

# print(str.capitalize())

# print(str.upper())


# print(str.replace("shakib", "sahib"))

# print(str.find("i"))

# print(str.count("i"))       

# str2 = "Hey i am shakib ansari";

# print(str2.find("shakib"));


# firstName = input("Enter your first name: ")

# print("Length of", firstName, len(firstName))

# str = input("Enter a string: ")

# print("Occurrence of $ is :", str.count("$"))

# my_name = "Shakib Ansari"

# print(my_name.upper())
# print(my_name.lower())
# print(my_name.casefold())
# print(my_name.center(60,"_"))
# print(my_name.count("i"))

# first_name = "Shakib "
# last_name = "Ansari - "
# print((first_name+last_name)*10)


# message = "hello"

# print(message)

# new_message = message.replace(message[0], "d")
# print(new_message)

# import re

# match = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumberjack')

# print(match.group(3))

# tags = "new, programming, things, gadgets, learning"
# tagList = tags.split(", ")

# for tag in tagList: 
#     print(tag)

# with open(r'C:\new\text.dat', 'w') as f: 
#     print(f)

# path = r"C:\new\text.data"
# print(len(path))


# myJob = "HACKER"

# for i in myJob: 
#     print(i, end=" $ ")

# str = "shakib"

# print(str[::-1])


# def print_message(message): 
#     print("The Message is: %s"%(message))

# print_message("Hey guys how are you...")

# str = "Hello" \
# "World" \
# "I am " \
# "New Here"

# print(str)

# str = """Hello 
# World
# I Am
# New Here"""

# print(str)

str = "        Hello           "
print(str)
new_str = str.strip()

print(new_str)
