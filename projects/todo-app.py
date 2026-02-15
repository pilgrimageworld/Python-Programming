import json
next_id = 1

while True: 
    choice = int(input("1. Add Todo\n2. Delete Todo\n3. Show Todos\nAny For Exit\n"))

    match choice: 
        case 1: 
            todo = input("Enter your Todo: ")

            try:
                with open("todo_list.json", "r") as f:
                    todo_list = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                todo_list = []

            todo_list.append({"id": next_id, "todo": todo})
            next_id += 1

            with open("todo_list.json", "w") as f:
                json.dump(todo_list, f)

        case 2:
            try:
                with open("todo_list.json", "r") as f:
                    todo_list = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                todo_list = []

            if not todo_list: 
                print("No Todo Added Yet!!!")
                continue

            id = int(input("Enter Todo Id to Delete: "))
            for todo in todo_list: 
                if todo['id'] == id:
                    todo_list.remove(todo)
                    with open("todo_list.json", "w") as f:
                        json.dump(todo_list, f)

        case 3: 
            try:
                with open("todo_list.json", "r") as f:
                    todo_list = json.load(f)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                todo_list = []

            if not todo_list:
                print("No Todo Added Yet!!!")
                continue
            
            for todo in todo_list:
                print(todo)               

        case _: 
            break
        

