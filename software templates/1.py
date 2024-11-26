class TodoModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks
class TodoView:
    def show_tasks(self, tasks):
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        if not tasks:
            print("The list is empty.")

    def show_message(self, message):
        print(message)
class TodoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, task):
        self.model.add_task(task)
        self.view.show_message(f"Task '{task}' added.")

    def remove_task(self, task_number):
        tasks = self.model.get_tasks()
        if 0 < task_number <= len(tasks):
            task = tasks.pop(task_number - 1)
            self.view.show_message(f"Task '{task}' removed.")
        else:
            self.view.show_message("Invalid task number!")

    def show_tasks(self):
        tasks = self.model.get_tasks()
        self.view.show_tasks(tasks)
def main():
    model = TodoModel()
    view = TodoView()
    controller = TodoController(model, view)

    while True:
        print("\nOptions: [1] Show tasks [2] Add task [3] Remove task [4] Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            controller.show_tasks()
        elif choice == '2':
            task = input("Enter a task: ")
            controller.add_task(task)
        elif choice == '3':
            try:
                task_number = int(input("Enter the task number to remove: "))
                controller.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
