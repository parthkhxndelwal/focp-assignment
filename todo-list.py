# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' has been added.")

# Function to remove a task from the list
def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return

    print("Tasks in the list:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    try:
        task_number = int(input("Enter the number of the task to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' has been removed.")
        else:
            print("Invalid task number. Please choose a valid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to view all tasks in the list
def view_tasks():
    if tasks:
        print("Tasks in the list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the list.")

# Main loop for the to-do list application
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        remove_task()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4).")
