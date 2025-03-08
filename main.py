import sys
import json
from datetime import datetime

def add_task(description: str):
    tasks = []
    try:
        file = open("data.json", "r")
        tasks = json.load(file)
    except FileNotFoundError:
        print("No data file found.")
        tasks = []
    except json.JSONDecodeError:
        print("No data in file")
        tasks = []
    
    with open("data.json", "w") as file:
        task_id = 1
        if len(tasks) > 0:
            task_id = max(tasks, key=lambda x: x["id"])["id"] + 1
        tasks.append({
            "id" : task_id,
            "description" : description,
            "status" : "todo",
            "createdAt" : datetime.now().strftime("%H:%M:%S %m-%d-%Y"),
            "updatedAt" : datetime.now().strftime("%H:%M:%S %m-%d-%Y"),
        })
        json.dump(tasks, file)
        print("Task added successfully (ID: ", task_id, ")")
            

def update_task_des(id: int, description: str):
    print("placeholder")
    #TODO

def update_task_status(id: int, status: str):
    print("placeholder")

def delete_task(id: int):
    print("placeholder")
    #TODO

def list_tasks(options = "all"):
    print("placeholder")
    #TODO

def main():
    arg_len = len(sys.argv)
    command = ""
    if arg_len < 2:
        print("Please enter a command")
        sys.exit(1)
    command = sys.argv[1]

    if arg_len == 3 and sys.argv[1] == "add":
        add_task(sys.argv[2])
    elif arg_len == 4 and sys.argv[1] == "update":
        update_task_des(sys.argv[2], sys.argv[3])
    elif arg_len == 3 and sys.argv[1] == "delete":
        delete_task(sys.argv[2])
    elif arg_len == 3 and command == "mark-in-progress":
        update_task_status(sys.argv[2], "in-progress")
    elif arg_len == 3 and command == "mark-done":
        update_task_status(sys.argv[2], "done")
    elif command == "list":
        if arg_len > 2:
            list_tasks()
        else:
            list_tasks(sys.argv[2])
    else:
        print("Please enter a valid command and all necessary arguments")

main()