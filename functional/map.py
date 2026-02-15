# nums = ['1', '2', '3', '4', '5']

# result = list(map(int, nums))

# print(result)

# message = ["Hey", "Guys", "How", "Are", "You"]

# def length(str): 
#     return len(str)

# result = list(map(length, message))

# print("Result: ", result)

# Give a list of integers, return a new list with each number squared.

# def square(num): 
#     return num ** 2


# nums = [1, 2, 3, 4, 5]

# result = list(map(square, nums))

# print(result)

# Find Square of a number using lambda expression

# nums = [1, 2, 3, 4, 5, 6, 7]

# result = list(map(lambda x: x*x, nums))
# print(result)


# Convert all strings in a list to uppercase.

# def upper_case(str): 
#     return str.upper()

# names = ["shakib", "sahal", "sahib", "arman"]
# result = list(map(upper_case, names))
# print("Result: ", result)

# Add 10 to every element in a list.

# def add_ten(num): 
#     return num+10

# nums = [5, 10, 15]

# result = list(map(add_ten, nums))

# print(result)

# Convert a list of temperatures from Celsius to Fahrenheit.

# def convert_temp_to_celsius(temp): 
#     return temp * (9/5)+32

# celsius = [0, 20, 37, 100]

# result = list(map(convert_temp_to_celsius, celsius))

# print(result)

# Get the first character of each string in a list.

# def get_first_char(str): 
#     return str[0]

# words = ["apple", "banana", "cherry"]

# result = list(map(get_first_char, words))

# print(result)

# Convert all numbers in a list to their absolute values.

# def convert_into_abs(num):
#     return abs(num)

# nums = [-5, -2, 0, 3, -10]

# result = list(map(convert_into_abs, nums))

# print(result)

# Add corresponding elements of two lists.

# def add_element(l1_ele, l2_ele): 
#     return l1_ele + l2_ele

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]

# result = list(map(add_element, l1, l2))

# print(result)


# Given a list of tuples, return a list containing the sum of each tuple.

# data = [(1, 2), (3, 4), (5, 6)]

# def sum_of_each_tuple(tup): 
#     sum = 0
#     for num in tup: 
#         sum += num
#     return sum

# result = list(map(sum_of_each_tuple, data))
# print(result)

# Extract domain names from email addresses.

# emails = ["user1@gmail.com", "user2@yahoo.com", "user3@outlook.com"]

# def extract_domain_name(email): 
#     idx = email.find("@")
#     return email[idx+1:]


# result = list(map(extract_domain_name, emails))
# print(result)


# Round each float to 2 decimal places.

# values = [3.14159, 2.71828, 1.41421]

# def round_two_places(value): 
#     return round(value, 2)


# result = list(map(round_two_places, values))
# print(result)


# Convert strings like "True" and "False" into actual boolean values.

# data = ["True", "False", "True"]

# def convert_true_false(value): 
#     if value == "True": 
#         return True
#     else: 
#         return False

# result = list(map(convert_true_false, data))

# print(result)


# Replace even numbers with "Even" and odd numbers with "Odd".

# nums = [1, 2, 3, 4, 5]

# def replace_by_words(num): 
#     if num%2==0: 
#         return "Even"
#     else: 
#         return "Odd"

# result = list(map(replace_by_words, nums))

# print(result)
