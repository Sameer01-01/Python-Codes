def display_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = []
    while True:
        print("\n1. Add Task")
        print("\n2. View Tasks")
        print("\n3. Remove Task")
        print("\n4. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            task = input("Enter task: ")
            tasks.append(task)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            task_num = int(input("Enter task number to remove: "))
            if 0 < task_num <= len(tasks):
                tasks.pop(task_num - 1)
            else:
                print("Invalid task number.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

main()
