# From a list of integers, keep only the even numbers.

# nums = [1, 2, 3, 4, 5, 6]

# nums = list(filter(lambda x: x%2 == 0, nums))
# print(nums)


# Keep only the positive numbers from a list.

# nums = [-5, 3, -1, 7, 0, -2]

# result = list(filter(lambda x: x > 0, nums))

# print(result)


# Remove empty strings from a list.

# words = ["apple", "", "banana", "", "cherry"]

# result = list(filter(lambda x: x != "", words))

# print(result)

# Keep words with more than 3 characters.

# words = ["cat", "lion", "tiger", "dog"]

# result = list(filter(lambda x: len(x) > 3, words))

# print(result)


# Keep numbers greater than 10.

# nums = [5, 12, 8, 20, 3, 15]

# result = list(filter(lambda x: x > 10, nums))

# print(result)

# Keep names that start with a vowel.

# names = ["Alice", "Bob", "Eve", "Oscar", "Charlie"]

# def check_vowels(name): 
#     first_char = name[0]
#     if first_char == "A" or first_char == "E" or first_char == "I" or first_char == "O" or first_char == "U": 
#         return name

# print(list(filter(check_vowels, names)))


# Keep emails that contain "@".

# emails = ["test@gmail.com", "invalidemail.com", "user@yahoo.com"]

# def remove_invalid_emails(email): 
#     return email.find("@") != -1


# print(list(filter(remove_invalid_emails, emails)))


# Print the range of prime number

# start_value = int(input("Enter Starting Value: "))
# end_value = int(input("Enter End Value: "))+1

# nums = [n for n in range(start_value, end_value)]

# def is_prime(num): 
#     count = 0

#     for i in range(1, num+1): 
#         if num%i == 0: 
#             count+=1

#     if count == 2: 
#         return True
    
#     else: 
#         return False
    
# prime_numbers = list(filter(is_prime, nums))

# print("Prime Number Range: ", prime_numbers)

