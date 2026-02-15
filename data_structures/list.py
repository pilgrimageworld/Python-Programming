# List is a sequence of collection that are positionally ordered and mutable which means lists can be modified in-place by assignment to offset as well as variaty of list function.


# list = [10, 20, 30, 40, 50]

# list.append(60)
# list.clear()
# list2 = list.copy()

# print("list: ", list)
# print("list 2: ", list2)
# list2[0] = 90
# print("list: ", list)
# print("list 2: ", list2)

# print(list.count(10))
# second_list = [2, 3, 4, 5]
# list.extend(second_list)

# print(list.index(40))

# list.insert(1, 19)

# list.remove(10)
# list.reverse()
# print(list)

# sort the list

# marks = [9, 1, 2, 8, 4, 4, 2, 1]

# marks.sort(reverse=True)
# print(marks)



# list = [2, 4, 6, 8, 10]

# list[9]= 9

# print(list)


# matrix = [[2, 3, 4], [1, 2, 3], [6, 7, 8]]
# for i in range(len(matrix)):
#     print(matrix[i])

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()
    

# Matrices

# size = int(input("Enter the size: "))

# matrix = []

# for i in range(size):
#     row = []
#     for j in range(size):
#         element = int(input("Enter the element: "))
#         row.append(element)
#     matrix.append(row)


# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()


# numbers = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]

# evenNumber = [x for x in numbers if x%2 == 0]

# print("Even Numbers: ", evenNumber)


matrix = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]

print("Normal Matrix", matrix)


flattenMatrix = [element for row in matrix for element in row]

print("Flatten Matrix", flattenMatrix)
