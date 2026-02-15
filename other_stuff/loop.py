
# count = 1

# while(count <= 10):
#     print("Count: ", count)
#     count += 1

# print(count)

# num = int(input("Enter a number: "))

# rev = 0

# while(num > 0):
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10
#     print(num)

# print(rev)

# n = int(input("Enter the n: "))
# i = 1
# while(i <= 10):
#     print(n," * ",i, " = ", n*i )
#     i += 1
    

# diff = 3
# num = 1
# while(num <= 100):
#     print(num)
#     num += diff
#     diff += 2

# Search for a number x in this tuple using loop


# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = int(input("Enter x: "))

# i = 0
# while i <= 9:
#     if x == tup[i]:
#         print("X exists")
#         break
#     i += 1

# if i > 9:
#     print("X not exists")
    

# fruits = ["Apple", "Banana" ,"Mango", "Orange"]

# for fruit in fruits:
#     print(fruit) 

# list = ["Hey", "Listen", "Me", "Carefully"]

# for item in list: 
#     if item == "You": 
#         print("Me Found")
#         break
#     print(item)
# else: 
#     print("END")


# Print the elements of the following list using a loop

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = int(input("Enter x: "))
# for t in tup :
#     if t == x :
#         print("x found")
#         break

# else: 
#     print("x not found")

# Range function

# for el in range(3, 33, 3): 
#     print(el)
    

# for el in range(1, 10, 3):
#     print(el)

# print(range(2, 10))


# for n in range(100, 0, -1):
#     print(n)


# n = int(input("Enter n: "))

# for i in range(n, n*11, n):
#     print(i)


# for i in range(5):
#     pass

# print("Something")


# Write a program to find the sum of first n numbers. 

# n = int(input("Enter n: "))
# sum = 0

# # n = 10 => 0+1+
# i = 0
# while (n >= 0):
#     sum += i
#     n -= 1
#     i += 1
# print(sum)


# Write a program to find the factorial of first n number


n = int(input("Enter n: "))
i = 1
fact = 1
for i in range(1, n+1): 
    fact = fact * i
print(fact)