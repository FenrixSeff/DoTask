# DoTask

**DoTask** is a simple Python CLI tool to manage personal to-do lists. Works on Termux and Unix-based terminals.

**DoTask** adalah alat CLI Python sederhana untuk mengelola daftar tugas. Berfungsi di Termux dan terminal berbasis Unix.

---

## Features | Fitur
-  Add tasks with custom status
-  View all tasks
-  Mark tasks as finished
-  Edit/delete tasks
-  Automatic JSON storage

-  Tambah tugas dengan status kustom
-  Lihat semua tugas
-  Tandai tugas selesai
-  Edit/hapus tugas
-  Penyimpanan otomatis format JSON

---

## Requirements | Persyaratan
- Python 3

## Installation | Instalasi
```bash
pkg install git python
git clone https://github.com/FenrixSeff/DoTask.git
cd DoTask
./setup
```

## Command-Line Usage | Penggunaan CLI
```bash
# Add task
dotask --add --name "Tidoo" --stat "8 jam/hari" -y

# Mark task as finished (no.3)
dotask --finished 3 -y

# Edit task (no.2)
dotask --change 2 --name "Nonton Nartoooo" --stat "epsd 391" -y

# Find tasks
dotask --find "RRQ Samsudin"

# Delete task (no.4)
dotask --delete 4 -y

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
[1] Show tasks
[2] Add task
[3] Edit task
[4] Delete task
[0] Exit
```

## Argparse Tutorial | Panduan Argparse
DoTask uses Python's argparse module for CLI. Key patterns:

**1. Mutually Exclusive Commands**
Commands that can't be used together:
```python
group = parser.add_mutually_exclusive_group()
group.add_argument("--add", action="store_true")
group.add_argument("--delete", type=int)
```

**2. Argument Types**
Specify data types for arguments:
```python
parser.add_argument("--name", type=str)
parser.add_argument("--finished", type=int)
```

**3. Optional Flags**
Flags without values:
```python
parser.add_argument("-y", "--yes", action="store_true")
```

**4. Help Messages**
Add descriptions for arguments:
```python
parser.add_argument("--find", help="Search tasks by name")
```

**5. Positional vs Optional**
- Positional: `dotask show` (no prefix)
- Optional: `dotask --delete 3` (with -- prefix)

---

## Storage | Penyimpanan
- Active tasks: `~/.dotask_notes.json`
- Deleted tasks: `~/.dotask_trash.json`

- Tugas aktif: `~/.dotask_notes.json`
- Tugas terhapus: `~/.dotask_trash.json`

## Notes | Catatan
Early development stage - fitur mungkin berubah
Tahap pengembangan awal - fitur mungkin berubah

---

## Author | Penulis
Fenrix
**License**: Open-source (free to use/modify)
