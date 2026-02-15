# name = "Shakib"

# it = iter(name)

# print(type(it))

# for i in it: 
#     print(i)


# nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# itr = iter(nums)

# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))


# values = [1, 3, 5, 7, 9]

# itr = iter(values)

# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))


# for x in [10, 20, 30, 40, 50]: 
#     print(x)

# Under the hood this happining

# it = iter([10, 20, 30, 40, 50])

# while True: 
#     try: 
#         x = next(it)
#         print(x)
#     except StopIteration: 
#         break
        

# Lets implement the __init__ and __next__

# class CountUp: 
#     def __init__(self, max): 
#         self.max = max
#         self.current = 1

#     def __iter__(self): 
#         return self

#     def __next__(self):
#         if self.current <= self.max: 
#             num = self.current
#             self.current += 1
#             return num
#         else: 
#             raise StopIteration
        

# itr = CountUp(1000)

# for i in itr: 
#     print(i, end=" | ")


# Write a function is_iterator(obj) that returns True if the object is an iterator, otherwise False.

# Hint: Iterators return themselves from __iter__().

# def is_iterator(obj):
#     try: 
#         if iter(obj): 
#             return True
#     except TypeError: 
#             return False

# print(is_iterator(obj="10"))

# Given a list [10, 20, 30], iterate over it without using a for loop.

# nums = [10, 20, 30]

# idx = 0

# while idx < len(nums): 
#     element = nums[idx]
#     print(element)
#     idx += 1

# What will be the output of this code?

# it = iter([1, 2])
# print(next(it))
# print(next(it))
# print(next(it))


# Create Custom Python Range. 

# for i in range(1, 2, 3,)

# def Range(stop, start: int = 0,  step: int = 1):
#     while start < stop: 
#         yield start
#         start += step

# for i in Range(10): 
#     print(i)


# Create an iterator that yields only even numbers from a given list.

# nums = [1,2, 3, 4, 5, 6, 7, 8]

# def even_itr(nums): 
#     for i in nums: 
#         if i%2 == 0: 
#             yield i


# itr = even_itr(nums)

# for num in itr: 
#     print(num)

