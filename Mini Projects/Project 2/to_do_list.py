#Create a command-line To-Do List app that lets users add, view, and delete tasks during a session.

todo_list = []

def add(task):
    todo_list.append(task)
    print("Task added")

def view():
    if not todo_list:
        print("No tasks yet")

    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def delete(index):
    if 0 < index <= len(todo_list):
        removed = todo_list.pop(index -1)
        print(f"Deleted: {removed}")

    else:
        print("Invalid Syntax")

if __name__ == "__main__":

    while(True):
        print("\n=== To-Do List ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view()
        elif choice == '2':
            task = input("Enter task: ")
            add(task)
        elif choice == '3':
            view()
            try:
                idx = int(input("Enter task number to delete: "))
                delete(idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Goodbye!")
        else:
            print("Invalid option.")