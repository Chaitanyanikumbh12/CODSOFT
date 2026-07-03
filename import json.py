import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['task']}")

# Add task
def add_task(tasks):
    task_name = input("Enter task: ")
    tasks.append({"task": task_name, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

# Update task
def update_task(tasks):
    view_tasks(tasks)

    try:
        task_no = int(input("Enter task number to update: "))
        new_task = input("Enter new task description: ")

        tasks[task_no - 1]["task"] = new_task
        save_tasks(tasks)
        print("Task updated successfully!")

    except:
        print("Invalid task number!")

# Complete task
def complete_task(tasks):
    view_tasks(tasks)

    try:
        task_no = int(input("Enter task number completed: "))
        tasks[task_no - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")

    except:
        print("Invalid task number!")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)

    try:
        task_no = int(input("Enter task number to delete: "))
        tasks.pop(task_no - 1)
        save_tasks(tasks)
        print("Task deleted successfully!")

    except:
        print("Invalid task number!")

# Main Program
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            update_task(tasks)

        elif choice == "4":
            complete_task(tasks)

        elif choice == "5":
            delete_task(tasks)

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()