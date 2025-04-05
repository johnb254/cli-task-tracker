# Task Tracker

This project was created as a part of [roadmap.sh](https://roadmap.sh)'s backend project series. It
was developed as a tool for me to improve as a backend and fullstack developer. It is based off the
[instructions](https://roadmap.sh/projects/task-tracker) posted on their website.

This is a task tracker that users interface with through the command line. It runs in a python
virtual environment and stores data in a json data file within the project folder.

## Setup
Ensure that your device has Python 3 installed and that the version is 3.8 or greater.

Download the main.py file of this project. In the same directory we're going to open the command
line and input the following command:
```powershell
python -m venv "task-cli"
```
Our virtual Python environment is now ready for use.

## Usage
In our virtual environment, we will run commands as follows:
```powershell
python main.py <command>
```

We have the following commands available:

- `add <description>`: Adds a new task with the given description.
- `update <id> <description>`: Updates the task with the given id's description.
- `delete <id>`: Removes the task with the given id from the data file.
- `mark-in-progress <id>`: Updates the status of the task with the given id to "in-progress".
- `mark-done <id>`: Updates the status of the task with the given id to "done".
- `list [done|todo|in-progress]`: Lists tasks in the data file. When options given, filters list by
  status
