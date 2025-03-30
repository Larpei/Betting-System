# Simple To-Do List in Python

tasks = []  # List to store tasks

def show_tasks():
    if not tasks:
        print("\nNo tasks added yet!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def delete_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            print(f"Deleted task: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

while True:
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1-4.")
