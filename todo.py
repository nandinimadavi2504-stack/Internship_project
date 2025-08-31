import json
import os

FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# Add new task
def add_task(name):
    tasks = load_tasks()
    tasks.append({"task": name, "done": False})
    save_tasks(tasks)
    print("Task added:", name)

# Show all tasks
def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour To-Do List:")
    for i, t in enumerate(tasks, 1):
        status = "Done" if t["done"] else "Pending"
        print(f"{i}. {t['task']} [{status}]")

# Delete a task
def delete_task(num):
    tasks = load_tasks()
    if 0 < num <= len(tasks):
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print("Deleted:", removed['task'])
    else:
        print("Task not found.")

# Mark task as done
def mark_done(num):
    tasks = load_tasks()
    if 0 < num <= len(tasks):
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Marked as done:", tasks[num - 1]['task'])
    else:
        print("Task not found.")

# Menu
def menu():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            task = input("Enter new task: ").strip()
            if task:
                add_task(task)
            else:
                print("Task cannot be empty.")
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            try:
                n = int(input("Enter task number to delete: "))
                delete_task(n)
            except ValueError:
                print("Enter a valid number.")
        elif choice == "4":
            try:
                n = int(input("Enter task number to mark done: "))
                mark_done(n)
            except ValueError:
                print("Enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
