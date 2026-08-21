from task import Task


class TodoManager:
    def __init__(self):
        # A list is used to store all Task objects.
        self.tasks = []

    def add_task(self, title):
        if not title.strip():
            return False

        task = Task(title.strip())
        self.tasks.append(task)
        return True

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
            return

        print("\n========== YOUR TASKS ==========")

        for number, task in enumerate(self.tasks, start=1):
            print(f"{number}. {task}")

        print("===============================")

    def remove_task(self, task_number):
        if task_number < 1 or task_number > len(self.tasks):
            return False

        self.tasks.pop(task_number - 1)
        return True

    def complete_task(self, task_number):
        if task_number < 1 or task_number > len(self.tasks):
            return False

        self.tasks[task_number - 1].mark_completed()
        return True
    
    
    