class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['description']} - {'Done' if task['done'] else 'Pending'}")

    def add_task(self):
        description = input("Enter task description: ")
        self.tasks.append({"description": description, "done": False})
        print("Task added successfully.")

    def update_task(self):
        self.display_tasks()
        try:
            task_number = int(input("Enter task number to update: ")) - 1
            if task_number < 0 or task_number >= len(self.tasks):
                print("Invalid task number.")
            else:
                new_description = input("Enter new task description: ")
                self.tasks[task_number]["description"] = new_description
                print("Task updated successfully.")
        except ValueError:
            print("Invalid task number.")

    def delete_task(self):
        self.display_tasks()
        try:
            task_number = int(input("Enter task number to delete: ")) - 1
            if task_number < 0 or task_number >= len(self.tasks):
                print("Invalid task number.")
            else:
                del self.tasks[task_number]
                print("Task deleted successfully.")
        except ValueError:
            print("Invalid task number.")

    def mark_as_done(self):
        self.display_tasks()
        try:
            task_number = int(input("Enter task number to mark as done: ")) - 1
            if task_number < 0 or task_number >= len(self.tasks):
                print("Invalid task number.")
            else:
                self.tasks[task_number]["done"] = True
                print("Task marked as done.")
        except ValueError:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Done")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            todo_list.display_tasks()
        elif choice == "2":
            todo_list.add_task()
        elif choice == "3":
            todo_list.update_task()
        elif choice == "4":
            todo_list.delete_task()
        elif choice == "5":
            todo_list.mark_as_done()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

