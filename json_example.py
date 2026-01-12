import json

person = {"name": "Shakib", "age": 19, "work": "Web Dev"}


new_person = json.dumps(person, indent=2)
print(new_person)