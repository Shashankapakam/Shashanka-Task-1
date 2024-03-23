class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. [{task['status']}] {task['name']}")

    def add_task(self, name):
        self.tasks.append({'name': name, 'status': 'Incomplete'})

    def mark_task_completed(self, task_num):
        if 1 <= task_num <= len(self.tasks):
            self.tasks[task_num - 1]['status'] = 'Completed'
            print(f"Task '{self.tasks[task_num - 1]['name']}' marked as completed.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_num):
        if 1 <= task_num <= len(self.tasks):
            del self.tasks[task_num - 1]
            print("Task removed successfully.")
        else:
            print("Invalid task number.")


def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task_name = input("Enter task name: ")
            todo_list.add_task(task_name)
            print("Task added successfully.")
        elif choice == '3':
            todo_list.display_tasks()
            task_num = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_task_completed(task_num)
        elif choice == '4':
            todo_list.display_tasks()
            task_num = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_num)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
