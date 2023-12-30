import time
ToDo = []
process = True

while process:
    print("type in 'help' to view commands")
    command = input(">").lower().strip()
    if command == "help":
        print("""
quit - to end the process
add - to add something to your todo list
remove - to remove something from your list
clear all - to remove everything from the list
show - to show your list
              """)

    if command == "add":
        adder = input("Add ToDo: ")
        ToDo.append(adder)
    elif command == "remove":
        print(ToDo)
        remover = input("remove Todo: ")
    elif command == "clear all":
        ToDo.clear()
        print("Todo List cleared.")
    elif command == "show":
        print(ToDo)
    elif command == "quit":
        exit()