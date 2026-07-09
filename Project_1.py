import json
import os

FILE_NAME = "tasks.json"


# --------------------------
# DATA LAYER (MODEL)
# --------------------------

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task_name = input("Enter task: ")

    task = {
        "id": len(tasks) + 1,
        "task": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\n========== TASK LIST ==========")

    for index, task in enumerate(tasks, start=1):

        status = "Completed" if task["completed"] else "Pending"

        print(f"""
Task No : {index}
ID      : {task['id']}
Task    : {task['task']}
Status  : {status}
-------------------------------
""")


def update_task(tasks):

    view_tasks(tasks)

    if not tasks:
        return

    task_id = int(input("Enter Task ID to update: "))

    for task in tasks:

        if task["id"] == task_id:

            new_task = input("Enter new task: ")
            task["task"] = new_task

            save_tasks(tasks)

            print("Task Updated Successfully.")
            return

    print("Task not found.")


def complete_task(tasks):

    view_tasks(tasks)

    if not tasks:
        return

    task_id = int(input("Enter Task ID to mark completed: "))

    for task in tasks:

        if task["id"] == task_id:

            task["completed"] = True

            save_tasks(tasks)

            print("Task Completed.")
            return

    print("Task not found.")


def delete_task(tasks):

    view_tasks(tasks)

    if not tasks:
        return

    task_id = int(input("Enter Task ID to delete: "))

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            for index, item in enumerate(tasks, start=1):
                item["id"] = index

            save_tasks(tasks)

            print("Task Deleted Successfully.")

            return

    print("Task not found.")


# --------------------------
# USER INTERFACE (VIEW)
# --------------------------

def menu():

    print("""
==============================
        TO-DO LIST
==============================

1. Add Task
2. View Tasks
3. Update Task
4. Complete Task
5. Delete Task
6. Exit

==============================
""")


# --------------------------
# MAIN PROGRAM
# --------------------------

def main():

    tasks = load_tasks()

    while True:

        menu()

        choice = input("Enter Choice : ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            update_task(tasks)

        elif choice == "4":
            complete_task(tasks)

        elif choice == "5":
            delete_task(tasks)

        elif choice == "6":
            print("Thank You.")
            break

        else:
            print("Invalid Choice.")


if __name__ == "__main__":
    main()