import Tasks,json
from colorama import init, Fore, Style

init(autoreset=True)

def successMessage(message):
    print(Fore.GREEN + f"\n✓ {message}")

def errorMessage(message):
    print(Fore.RED + f"\n✗ {message}")

def infoMessage(message):
    print(Fore.CYAN + f"\n» {message}")


def addTask():
    task = {
        "title": input("Task title: ").strip(),
        "subject": input("Subject: ").strip(),
        "priority": input("Priority: ").capitalize(),
        "status": input("Status: ").capitalize()
    }
    while task["title"].strip() == "":
        infoMessage("Title cannot be empty. Please enter a valid title.")
        task["title"] = input("Task title: ")

    while any(existing_task["title"].lower() == task["title"].lower() for existing_task in Tasks.tasks):
        infoMessage("A task with this title already exists. Please enter a different title.")
        task["title"] = input("Task title: ").strip()
        while task["title"].strip() == "":
            infoMessage("Title cannot be empty. Please enter a valid title.")
            task["title"] = input("Task title: ")

    while task["subject"].strip() == "":
        infoMessage("Subject cannot be empty. Please enter a valid subject.")
        task["subject"] = input("Subject: ")

    while task["priority"] not in ["High", "Medium", "Low"]:
        infoMessage("Invalid priority. Please enter High, Medium, or Low.")
        task["priority"] = input("Priority: ").capitalize()

    while task["status"] not in ["Completed", "Pending", "Canceled"]:
        infoMessage("Invalid status. Please enter Completed, Pending, or Canceled.")
        task["status"] = input("status: ").capitalize()

    Tasks.tasks.append(task)
    successMessage("Task added successfully!")

    saveTasks()
    # task_json = json.dumps(Tasks.tasks)
    # print(task_json)
    # restored_tasks = json.loads(task_json)
    # print(restored_tasks[0]["title"])


def viewTasks():
    if not Tasks.tasks:
        errorMessage("No tasks available.")
        return
    
    for task in sorted(Tasks.tasks,key=lambda x: ["High","Medium","Low"].index(x["priority"])): 

        print(Fore.CYAN + "┌──────────────────────────────────────┐")
        print(Fore.CYAN + "│" + Fore.YELLOW + f" Title    : {task['title']:<26}" + Fore.CYAN + "│")
        print(Fore.CYAN + "│" + Fore.GREEN + f" Subject  : {task['subject']:<26}" + Fore.CYAN + "│")
        print(Fore.CYAN + "│" + Fore.MAGENTA + f" Priority : {task['priority']:<26}" + Fore.CYAN + "│")
        print(Fore.CYAN + "│" + Fore.BLUE + f" Status   : {task['status']:<26}" + Fore.CYAN + "│")
        print(Fore.CYAN + "└──────────────────────────────────────┘")


        

def searchTask():
    searchTitle = input("Enter the title of the task to search: ").strip()
    found = False

    for task in Tasks.tasks:
        if task["title"].lower() == searchTitle.lower():
            print(Fore.GREEN + "\n✓ Task found!")

            print(Fore.CYAN + "┌──────────────────────────────────────┐")
            print(Fore.CYAN + "│" + Fore.YELLOW + f" Title    : {task['title']:<26}" + Fore.CYAN + "│")
            print(Fore.CYAN + "│" + Fore.BLUE + f" Subject  : {task['subject']:<26}" + Fore.CYAN + "│")

            priority_color = {
                "High": Fore.RED,
                "Medium": Fore.YELLOW,
                "Low": Fore.GREEN
            }.get(task["priority"], Fore.WHITE)

            status_color = {
                "Completed": Fore.GREEN,
                "Pending": Fore.YELLOW,
                "Canceled": Fore.RED
            }.get(task["status"], Fore.WHITE)

            print(Fore.CYAN + "│" + priority_color + f" Priority : {task['priority']:<26}" + Fore.CYAN + "│")
            print(Fore.CYAN + "│" + status_color + f" Status   : {task['status']:<26}" + Fore.CYAN + "│")
            print(Fore.CYAN + "└──────────────────────────────────────┘")

            found = True
            break

    if not found:
        errorMessage("Task not found.")


def updateTask():
    updateTitle = input("Enter the title of the task to update: ")
    found = False
    update = False
    for task in Tasks.tasks:
        if task["title"].lower() == updateTitle.lower():
            print("1. Update Title \n2. Update Subject \n3. Update Priority \n4. Update Status")
            choice = input("Enter your choice for update: ")

            if choice == "1":
                task["title"] = input("Enter new title: ").strip()
                while task["title"].strip() == "":
                    infoMessage("Title cannot be empty. Please enter a valid title.")
                    task["title"] = input("Task title: ").strip()
                
                while any(existing_task["title"].lower() == task["title"].lower() for existing_task in Tasks.tasks):
                    infoMessage("A task with this title already exists. Please enter a different title.")
                    task["title"] = input("Task title: ").strip()
                    while task["title"].strip() == "":
                        infoMessage("Title cannot be empty. Please enter a valid title.")
                        task["title"] = input("Task title: ")
                successMessage("Task updated successfully!")
                update = True

            elif choice == "2":
                task["subject"] = input("Enter new subject: ").strip()
                while task["subject"].strip() == "":
                    infoMessage("Subject cannot be empty. Please enter a valid subject.")
                    task["subject"] = input("Subject: ").strip()
                successMessage("Task updated successfully!")
                update = True

            elif choice == "3":
                task["priority"] = input("Enter new priority: ").capitalize()
                while task["priority"] not in ["High", "Medium", "Low"]:
                    infoMessage("Invalid priority. Please enter High, Medium, or Low.")
                    task["priority"] = input("Priority: ").capitalize()
                successMessage("Task updated successfully!")
                update = True

            elif choice == "4":
                task["status"] = input("Enter new status: ").capitalize()
                while task["status"] not in ["Completed", "Pending", "Canceled"]:
                    infoMessage("Invalid status. Please enter Completed, Pending, or Canceled.")
                    task["status"] = input("status: ").capitalize()
                successMessage("Task updated successfully!")
                update = True

            else:
                errorMessage("Invalid choice.")
            
            if update:
                saveTasks()
            found = True
            break
    if not found:
        errorMessage("Task not found.")


def deleteTask():
    delTitle = input("Enter the title of the task to delete: ")
    found = False
    for task in Tasks.tasks:
        if task["title"].lower() == delTitle.lower():
            Tasks.tasks.remove(task)
            saveTasks()
            successMessage("Task deleted successfully!")
            found = True
            break
    
    if not found:
        errorMessage("Task not found.")


def completedTasks():
    completed = [
        task for task in Tasks.tasks
        if task["status"].lower() == "completed"
    ]

    if not completed:
        errorMessage("No completed tasks available.")
        return

    print(Fore.GREEN + f"\n✓ Completed Tasks: {len(completed)}")

    for task in completed:
        print(Fore.CYAN + "┌──────────────────────────────────────┐")
        print(Fore.CYAN + "│" + Fore.YELLOW + f" Title    : {task['title']:<26}" + Fore.CYAN + "│")
        print(Fore.CYAN + "│" + Fore.GREEN + f" Subject  : {task['subject']:<26}" + Fore.CYAN + "│")
        print(Fore.CYAN + "│" + Fore.MAGENTA + f" Priority : {task['priority']:<26}" + Fore.CYAN + "│")
        print(Fore.CYAN + "│" + Fore.GREEN + f" Status   : {task['status']:<26}" + Fore.CYAN + "│")
        print(Fore.CYAN + "└──────────────────────────────────────┘")



def taskStatistics():
    total_tasks = len(Tasks.tasks)
    completed_tasks = len([task for task in Tasks.tasks if task["status"].lower() == "completed"])
    pending_tasks = len([task for task in Tasks.tasks if task["status"].lower() == "pending"])
    canceled_tasks = len([task for task in Tasks.tasks if task["status"].lower() == "canceled"])

    print(Fore.CYAN + "\n╔══════════════════════════════════╗")
    print(Fore.CYAN + "║         TASK STATISTICS          ║")
    print(Fore.CYAN + "╠══════════════════════════════════╣")
    print(Fore.WHITE + f"║ Total Tasks     : {total_tasks:<15}║")
    print(Fore.GREEN + f"║ Completed Tasks : {completed_tasks:<15}║")
    print(Fore.YELLOW + f"║ Pending Tasks   : {pending_tasks:<15}║")
    print(Fore.RED + f"║ Canceled Tasks  : {canceled_tasks:<15}║")
    print(Fore.CYAN + "╚══════════════════════════════════╝")



def getChoice():
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        errorMessage("Invalid input. Please enter a number.")
        return None
   

def menu():
    while True:
        print(Fore.CYAN + "\n╔══════════════════════════════════════╗")
        print(Fore.CYAN + "║           SMART STUDY                ║")
        print(Fore.CYAN + "║           TASK MANAGER               ║")
        print(Fore.CYAN + "╠══════════════════════════════════════╣")
        print(Fore.WHITE + "║  [1] Add Task       [2] View Tasks   ║")
        print(Fore.WHITE + "║  [3] Search Task    [4] Update Task  ║")
        print(Fore.WHITE + "║  [5] Delete Task    [6] Completed    ║")
        print(Fore.WHITE + "║  [7] Statistics     [8] Exit         ║")
        print(Fore.CYAN + "╚══════════════════════════════════════╝")

        choice = getChoice()

        if choice is None:
            continue

        if choice == 1:
            addTask()
        elif choice == 2:
            viewTasks()
        elif choice == 3:
            searchTask()
        elif choice == 4:
            updateTask()
        elif choice == 5:
            deleteTask()
        elif choice == 6:
            completedTasks()
        elif choice == 7:
            taskStatistics()
        elif choice == 8:
            break
        else:
            errorMessage("Invalid choice. Please try again.")


def saveTasks():
    with open("tasks.json", "w") as file:
        json.dump(Tasks.tasks, file , indent=4)


def loadTasks():
    try:
        with open("tasks.json", "r") as file:
            Tasks.tasks = json.load(file)
    except FileNotFoundError:
        errorMessage("No tasks found. Starting with an empty task list.")
        Tasks.tasks = []
    except json.JSONDecodeError:
        errorMessage("Error decoding tasks.json. Starting with an empty task list.")
        Tasks.tasks = []