import csv
from datetime import datetime


class Task:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, '%d/%m/%Y')
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"Name: {self.name}, Start Date: {self.start_date.strftime('%d/%m/%Y')}, Priority: {self.priority}"
                f", Cost Estimate: {self.cost_estimate}, Completion Percentage: {self.completion_percentage}")


def load_tasks(filename):
    tasks = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            task = Task(*row)
            tasks.append(task)
    return tasks


def save_tasks(filename, tasks):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Start Date', 'Priority', 'Cost Estimate', 'Completion Percentage'])
        for task in tasks:
            writer.writerow([task.name, task.start_date.strftime('%d/%m/%Y'), task.priority, task.cost_estimate,
                             task.completion_percentage])


def display_tasks(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: (x.start_date, x.priority))
    incomplete_tasks = [task for task in sorted_tasks if task.completion_percentage < 100]
    completed_tasks = [task for task in sorted_tasks if task.completion_percentage == 100]

    print("\nUncompleted tasks:")
    for task in incomplete_tasks:
        print(task)

    print("\nCompleted tasks:")
    for task in completed_tasks:
        print(task)


def filter_tasks_by_date(tasks):
    date_str = input("Enter date (DD/MM/YYYY): ")
    try:
        filter_date = datetime.strptime(date_str, '%d/%m/%Y')
        filtered_tasks = [task for task in tasks if task.start_date >= filter_date]
        sorted_filtered_tasks = sorted(filtered_tasks, key=lambda x: (x.start_date, x.priority))

        print("\nTasks after the specified date:")
        for task in sorted_filtered_tasks:
            print(task)
    except ValueError:
        print("Invalid date format. Please use DD/MM/YYYY.")


def add_task(tasks):
    name = input("Enter task name: ")
    start_date = input("Enter start date (DD/MM/YYYY): ")
    priority = input("Enter priority: ")
    cost_estimate = input("Enter cost estimate: ")
    completion_percentage = input("Enter completion percentage: ")

    new_task = Task(name, start_date, priority, cost_estimate, completion_percentage)
    tasks.append(new_task)
    print("Task added successfully.")


def update_task(tasks):
    name = input("Enter the name of the task to update: ")
    found = False

    for task in tasks:
        if task.name == name:
            found = True
            print(task)
            completion_percentage = input("Enter new completion percentage (leave blank to keep existing value): ")
            priority = input("Enter new priority (leave blank to keep existing value): ")

            if completion_percentage:
                task.completion_percentage = int(completion_percentage)
            if priority:
                task.priority = int(priority)

            print("Task updated successfully.")
            break

    if not found:
        print("Task not found.")


def main():
    tasks = []
    while True:
        print("\n=== Menu ===")
        print("1. Load project")
        print("2. Save project")
        print("3. Display project")
        print("4. Filter tasks by date")
        print("5. Add new task")
        print("6. Update task")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter filename to load: ")
            tasks = load_tasks(filename)
            print("Project loaded successfully.")
        elif choice == "2":
            filename = input("Enter filename to save: ")
            save_tasks(filename, tasks)
            print("Project saved successfully.")
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            filter_tasks_by_date(tasks)
        elif choice == "5":
            add_task(tasks)
        elif choice == "6":
            update_task(tasks)
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()

