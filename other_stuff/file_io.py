# f = open("text.txt", "w")

# f.write("Hello World")

# f.close()

# f = open("text.txt", "r")

# line1 = f.readline()
# print("Line 1: ", line1)

# line2 = f.readline()
# print("Line 2: ", line2)

# f.close()

# f = open("text.txt", "r+")
# f.write("Hey ")

# print(f.read())
# f.close()


# with open("text.txt", "r") as f: 
#     print(f.read())
#     f.close()

# print(f.read())


# import os

# output = os.remove("./text.txt")
# print(output)

# with open("practice.txt", "w") as f: 
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")

# def replace(fileName): 
#     with open(fileName, "r") as f:
#         data = f.read()
#         new_data = data.replace("Java", "Python")
#     with open(fileName, "w") as f:
#         f.write(new_data) 
        
# replace("practice.txt")


# word = "learning"

# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:   
#         print("Not Found")
    


# From a file containing numbers seperated by comma, print the count of even numbers.

count = 0

with open("numbers.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums: 
        if (int(val) % 2 == 0):
            count += 1



print(count)

