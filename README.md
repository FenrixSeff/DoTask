# DoTask

**DoTask** is a simple Python CLI tool to manage personal to-do lists.

## Features | Fitur
-  Add tasks with custom status
-  View all tasks
-  Mark tasks as finished
-  Edit/delete tasks
-  Automatic JSON storage


## Requirements | Persyaratan
- Python 3

## Installation | Instalasi
```bash
pkg install git
git clone https://github.com/FenrixSeff/DoTask.git
cd DoTask
./setup
```

## Command-Line Usage | Penggunaan CLI
```bash
# Add task
dotask --add --name "Tidoooo" --stat "8 jam/hari" -y

# Mark task as finished (no.3)
dotask --finished 3 -y

# Edit task (no.2)
dotask --change 2 --name "marathon Nartoooo" --stat "epsd 391" -y

# if you want to change one of them
dotask --change 2 --stat "epsd 392" -y

# Find tasks
dotask --find "RRQ Samsudin"

# Delete task (no.4)
dotask --delete 4 -y

# if you want to delete all
dotask --delete 0 -A -y

# Show all tasks
dotask --show

# Restore deleted tasks (by date)
dotask --undo "03/07/25"
```

## Interactive Mode | Mode Interaktif
Just run `dotask` without arguments:
```bash
dotask
```
Then select options from the menu:
```
[1] To-do-List
[2] Add task
[3] Change task
[4] Delete task
[0] Exit
```

## Argparse Tutorial | Panduan Argparse
DoTask uses Python's argparse module for CLI. Key patterns:

**1. Mutually Exclusive Commands**
Commands that can't be used together:
```python
"--add"
"--delete"      # int
"--change"      # int
"--finished"    # int
"--undo"        # str
"--find"        # str
```

**2. Argument Types**
Specify data types for arguments:
```python
"--name"        # str
"--stat"        # str
```

**3. Optional Flags**
maybe just this:
```python
"--show"
"--yes", "-y"
"--select-all", "-A"
```

## Storage | Penyimpanan
- Active tasks: `~/.dotask_notes.json`
- Deleted tasks: `~/.dotask_trash.json`

## Notes | Catatan
Early development stage - fitur mungkin berubah

## Author | Penulis
Fenrix

**License**: Open-source (free to use/modify)
