num = int(input("Enter a number 1 - 5: "))

match num: 
    case 1: 
        print("User pressed 1")
    case 2: 
        print("User pressed 2")
    case 3: 
        print("User pressed 3")
    case 4: 
        print("User pressed 4")
    case 5: 
        print("User pressed 5")
    case _: 
        print("User pressed Unknown")

print("End of the program")