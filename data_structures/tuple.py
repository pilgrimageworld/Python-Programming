# Tuple is a ordered sequance of collection. It is immutable and cannot be modified.


# tuple = (1, 2, 3, 4, 5 )
# print(type(tuple))


# print(tuple.count(9))

# print(tuple)

# print(tuple.index(5))

# tuple = (10, 20, "Shakib", {"name": "John", "work": "system engineer"},(40, 50, (100, 200)))

# print(tuple)


# Why use tuple ?

def read_data(users): # It only read data for future.
    users[0] = {"name": "Rihan"}

users = ({"name": "shakib"}, {"name": "punit"}, {"name": "sameer"})

read_data(users)

print(users)