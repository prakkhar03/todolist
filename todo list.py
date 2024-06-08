class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.description}"


class ToDoList:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task number.")

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")

    def __str__(self):
        return self.name


class ToDoApp:
    def __init__(self):
        self.lists = {}

    def create_list(self, name):
        if name in self.lists:
            print("List already exists.")
        else:
            self.lists[name] = ToDoList(name)
            print(f"List '{name}' created.")

    def remove_list(self, name):
        if name in self.lists:
            del self.lists[name]
            print(f"List '{name}' removed.")
        else:
            print("List not found.")

    def use_list(self, name):
        if name in self.lists:
            self.manage_list(self.lists[name])
        else:
            print("List not found.")

    def manage_list(self, todo_list):
        while True:
            print(f"\nManaging List: {todo_list}")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. Mark Task as Complete")
            print("4. Show Tasks")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                description = input("Enter task description: ")
                todo_list.add_task(description)
                print("Task added.")
            elif choice == "2":
                todo_list.show_tasks()
                index = int(input("Enter task number to remove: ")) - 1
                todo_list.remove_task(index)
                print("Task removed.")
            elif choice == "3":
                todo_list.show_tasks()
                index = int(input("Enter task number to mark complete: ")) - 1
                todo_list.mark_task_complete(index)
                print("Task marked as complete.")
            elif choice == "4":
                todo_list.show_tasks()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def main_menu(self):
        while True:
            print("\nToDo List Application")
            print("1. Create List")
            print("2. Use List")
            print("3. Remove List")
            print("4. Quit")
            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter list name: ")
                self.create_list(name)
            elif choice == "2":
                name = input("Enter list name to use: ")
                self.use_list(name)
            elif choice == "3":
                name = input("Enter list name to remove: ")
                self.remove_list(name)
            elif choice == "4":
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = ToDoApp()
    app.main_menu()
