# Write a generator that yields the numbers from 1 to n.

# def one_to_n(n): 
#     for i in range(1, n+1): 
#         yield i


# one_to_n_generator = one_to_n(10)

# for val in one_to_n_generator: 
#     print(val, end=" ")

# Create a generator that yields all even numbers between 0 and 100.

# def even_numbers(): 
#     for i in range(100+1): 
#         if i%2 == 0: 
#             yield i

# even_numbers_generator = even_numbers()

# for val in even_numbers_generator: 
#     print(val, end=" ")


# Convert this function into a generator:
# def squares(n):
#     return [i*i for i in range(n)]

# print(squares(10))


# def squares(n): 
#     for i in range(n): 
#         yield i**2

# squares_generator = squares(10)

# for val in squares_generator: 
#     print(val, end=", ")

# Write a generator that yields the Fibonacci sequence up to n terms.

# 0, 1, 0+1=1, 1+1=2, 1+2=3, 2+3=5, 3+5=8, 5+8=13

# 0, 1, 1, 2, 3, 5, 8, 13


# def fibonacci(n):
    
#     first = 0
#     second = 1
#     yield first
#     yield second

#     for i in range(n-1): 
#         i = first+second
#         yield i
#         first = second
#         second = i

# fibonacci_generator = fibonacci(10)

# for val in fibonacci_generator: 
#     print(val, end=" ")


# Write a generator expression that yields squares of odd numbers from 1 to 50.

# def squares_of_odd(): 
#     for i in range(1, 59): 
#         if i%2 != 0: 
#             yield i ** 2

    
# squares_of_odd_generator = squares_of_odd()

# for val in squares_of_odd_generator: 
#     print(val, end=" ")



# Write a generator that reads a file line by line and yields only lines containing the word "error".

# def read_line(): 
#     try: 
#         with open("text.txt", "r") as f: 
#             data = f.read()
#             sentance = data.split("\n")
#         for line in sentance: 
#             idx = line.find("error")
#             if(idx != -1):
#                 yield line
            
#     except (FileNotFoundError): 
#         print("File Not Found")

# read_line_generator = read_line()

# for line in read_line_generator: 
#     print(line)
