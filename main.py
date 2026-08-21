from todo_manager import TodoManager


def display_menu():
    print("\n========================================")
    print("          TO-DO LIST MANAGER")
    print("========================================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")
    print("========================================")


def main():
    manager = TodoManager()

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        # Add Task
        if choice == "1":
            title = input("Enter task: ").strip()

            if manager.add_task(title):
                print("Task added successfully!")
            else:
                print("Task cannot be empty.")

        # View Tasks
        elif choice == "2":
            manager.view_tasks()

        # Remove Task
        elif choice == "3":
            try:
                task_number = int(
                    input("Enter task number to remove: ").strip()
                )

                if manager.remove_task(task_number):
                    print("Task removed successfully!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Invalid input. Please enter a number.")

        # Complete Task
        elif choice == "4":
            try:
                task_number = int(
                    input("Enter task number to complete: ").strip()
                )

                if manager.complete_task(task_number):
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Invalid input. Please enter a number.")

        # Exit
        elif choice == "5":
            print("Thank you for using To-Do List Manager!")
            break

        # Invalid menu option
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()