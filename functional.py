# Iterators

# str = "Shakib"

# it = iter(str)

# print(type(it))

# num = [2, 3, 4, 5, 6]

# it = iter(num)

# print(type(it))

# tup = ("Hello", "Guys", "How", "Are", "You")

# it = iter(tup)

# print(type(it))


# my_name = "Shakib"

# itr = iter(my_name)

# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# class EvenNumbers: 
#     def __iter__(self): 
#         self.n = 0
#         return self

#     def __next__(self): 
#         x = self.n + 2
#         self.n += 2
#         return x
    

# evenNum = EvenNumbers()

# itr = iter(evenNum)

# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# class OddNumbers: 
#     def __iter__(self): 
#         self.n = 1
#         return self

#     def __next__(self): 
#         x = self.n
#         self.n +=  2
#         return x
    

# oddNums = OddNumbers()

# itr = iter(oddNums)

# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

