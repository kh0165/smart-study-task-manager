# Smart Study & Task Manager

A terminal-based task management application built with Python to help students organize their study tasks and track their progress.

## Features

- Add new tasks with title, subject, priority, and status
- View all tasks sorted by priority
- Search for tasks by title
- Update task details
- Delete tasks
- View completed tasks
- Display task statistics
- Save and load tasks using JSON
- Colored terminal interface
- Input validation and duplicate task prevention

## Technologies Used

- Python
- JSON for data persistence
- Colorama for colored terminal output
- Git and GitHub for version control

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/kh0165/smart-study-task-manager.git
cd smart-study-task-manager
```

### 2. Create and activate a virtual environment

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install colorama
```

### 4. Run the application

```bash
python Main.py
```

## Task Options

### Priority Levels

- High
- Medium
- Low

### Task Statuses

- Pending
- Completed
- Canceled

## Data Storage

Tasks are stored locally in a JSON file named `tasks.json`, allowing the application to save and load task data between sessions.

## Project Goal

This project was built to practice Python fundamentals, including functions, lists, dictionaries, input validation, file handling, JSON, and modular code organization.

## Author

kh0165
