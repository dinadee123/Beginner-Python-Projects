tasks = []

while True:
    print("To-Do List")
    print("1. Add Your Task")
    print("2. View Your Tasks")
    print("3. Remove Your Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!!")

    elif choice == "2":
        print("Your Tasks: ")
        for t in tasks:
            print("-" + t)

    elif choice == "3":
        remove_task = input("Enter the task to remove : ")
        if remove_task in tasks:
            tasks.remove(remove_task)
            print("Task removed!")
        else:
            print("Task not found!")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
        
          
