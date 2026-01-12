# Find the Average of 3 numbers

# def avg_of_three(n1, n2, n3): 
#     return (n1+n2+n3)// 3

# print(avg_of_three(10, 20, 30))


# print("Heyy", end=" ")
# print("Guyss")

# print("Hey", "Dosto", sep="-")


# def calc_prod(a = 1, b = 1):
#     return a*b

# print(calc_prod())

# Write a program to print the length of a list.

"""
def print_list_len(list):
    print(len(list))
list = ["Shakib", "is", "a", "good", "programmer"]
print_list_len(list)
"""

# Write a function to print the elements of a list in a single line. 

"""
def print_list_element(list):
    print(list)
list = ["Shakib", "is", "a", "good", "programmer"]
print_list_element(list)
"""

# Write a function to find the factorial of n.
"""
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i

    return fact

print(factorial(5))
"""

# Write a function to convert USD to INR.

"""
def usd_to_inr(inr):
    return inr * 89.88

print(usd_to_inr(45760.21))
"""

# Recursion

# def show(n): 
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(10)


# Factorial using recuresion

def factorial(n): 
    if(n == 0 or n == 1):
        return n
    
    return (n * factorial(n-1))

print(factorial(5))