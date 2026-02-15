# Dictionary is a data collection that store data in the form of key value pair. It is mutable and not maintain order.

# dict = {
#     "name": "Shakib", 
#     "age": 19, 
#     "married_status": "single", 
#     "education": "Undergraduate"
# }
# print(dict)

# dict['married_status'] = "committed"
# print(dict)

student = {}

student["name"] = "John"
student["age"] = 19
student["marks"] = 89

# student.update({"name":"Shakib",  "marks": 76})


if('section' in student):
    print("Student Section: ", student["section"])