tasks = []

def view_tasks():
    print("Tasks:")
    with open("data.txt", "r") as file:
        for line_number, data in enumerate(file, start=1):
            print(f"{line_number}: {data.strip()}")
        print("\n")
        file.close()

    

    while True:
        userInput = int(input("Exit? (1) Yes\n"))
        
        try:
            if userInput == 1:
                main_menu()
            else: 
                print("-- Invalid Input. Please Try Again --")
                continue

        except ValueError:
            print("-- Invalid Input. Please Enter a Number --")
            

def add_tasks():
    task = input("Enter Task: ")

    with open("data.txt", "a") as file:
        file.write(task)
        file.write("\n")
        file.close()

    while True:
        try: 
            userInput = int(input("Add Another? (1) Yes (2) No"))
            if userInput == 1:
                add_tasks()
                break
            elif userInput == 2:
                main_menu()
                break
            else:
                print("-- Invalid Input. Please Try Again --")

        except ValueError:
            print("-- Invalid Input. Please Enter a Number --")



def remove_tasks():
    global tasks
    tasks.clear()
    with open("data.txt", "r") as file:
        tasks = file.readlines()

    for line_number, data in enumerate(tasks, start=1):
        print(f"{line_number}: {data.strip()}")
    print("\n")

    try:
        task_number_remove = int(input("Enter the task number to remove: "))
        if 1 <= task_number_remove <= len(tasks):
            del tasks[task_number_remove - 1]

            with open("data.txt", "w") as file:
                file.writelines(tasks)
            
            print(f"Task {task_number_remove} has been removed.")
            main_menu()
        else:
            print("-- Invalid Task Number. Please Try Again --")
            remove_tasks()
    except ValueError:
        print("-- Invalid Input. Please Enter a Number --")
        remove_tasks()










    


    



# Main Menu

def main_menu():
    userInput = int(input("(1) View All Tasks (2) Add a Task (3) Remove a Task  "))
    if userInput == 1:
        view_tasks()
    elif userInput == 2:
        add_tasks()
    elif userInput == 3:
        remove_tasks()
    else:
        print("-- Invalid Input. Please Try Again --")
        main_menu()
    




if __name__ == '__main__':
    main_menu()

