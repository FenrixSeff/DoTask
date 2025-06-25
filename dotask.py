#!/data/data/com.termux/files/usr/bin/env python3

from pathlib import Path
import subprocess as sub
import json
import time


def tasks(dft, msg):
    print(msg)
    for no, tugas in enumerate(dft):
        for nama, status in tugas.items():
            print(f"[{no + 1}] {nama} → {status}")
    if len(dft) > 0:
        print("")

    else:
        pass


def pix(task):
    while True:
        slct = input("Select number: ")
        if not slct.isdigit():
            pass
        elif int(slct) > 0 and int(slct) <= len(task):
            break

        print(outside)

    return int(slct)


def save(task):
    sure = input("You sure? (y/n): ")
    if sure.lower() == "y":
        with open(loc, "w") as f:
            json.dump(task, f, indent=4)
    else:
        pass


def laa():
    print("[!] Empty!")
    press = input("\nPress anywhere: ")


def clear():
    sub.run(["clear"])


opt = {
    "[1]": "To-Do-List",
    "[2]": "Add task",
    "[3]": "Change task",
    "[4]": "Delete task",
    "[0]": "Exit"
    }



loc = Path.home() / ".dotask_notes.json"
if not loc.exists():
    loc.touch()
    loc.write_text("[]")

outside = ("Enter the available number!\n")

while True:
    clock = time.strftime("[%H:%M]")

    clear()
    print(f"\n⟩—Option—⟨  {clock}\n")
    for opsi, isi in opt.items():
        print(f"{opsi} {isi}")


    while True:
        user = input("\nSelect option: ").strip()
        if user in["1", "2", "3", "4"]:
            break

        elif user == "0":
            print(
                 "\nVersion 02.05.8"
                 "\nBy Fenrix"
            )
            exit()
        print(outside)


    if user == "1":   # Daftar tugas dan tandai selesai
        clear()
        with open(loc, "r") as f:
            all_task = json.load(f)
            tasks(all_task, msg=f"\n⟩—To do list—⟨  {clock}\n")
        while True:
            rsp = input("What tasks have you just completed? "
                        "(N)one: ").strip()
            if rsp.lower() == "n":
                break

            elif not rsp.isdigit():
                print(outside)

            elif int(rsp) > len(all_task) or int(rsp) <= 0:
                print(outside)

            else:
                for i in all_task:
                    for t in i.keys():
                        task = t
                        stat = "Finished"
                        all_task.pop(int(rsp) - 1)
                        all_task.insert(int(rsp) -1, {task: stat})
                save(all_task)
                break


    elif user == "2":   # Tambah tugas
        clear()
        with open(loc, "r") as f:
            all_task = json.load(f)
            tasks(all_task, msg=f"\n⟩—Add task—⟨  {clock}\n")
            task = input("Task name: ").strip()
            stat = input("Status: ").strip()
            all_task.append({task: stat})
            save(all_task)


    elif user == "3":   # Rubah tugas
        clear()
        with open(loc, "r") as f:
            all_task = json.load(f)
            tasks(all_task, msg=f"\n⟩—Change task—⟨  {clock}\n")
        if len(all_task) == 0:
            laa()

        else:
            target = pix(all_task)
            task = input("Task name: ").strip()
            stat = input("Status: ").strip()
            all_task.pop(target - 1)
            all_task.insert(target - 1, {task: stat})
            save(all_task)


    elif user == "4":   # Hapus tugas
        clear()
        with open(loc, "r") as f:
            all_task = json.load(f)
            tasks(all_task, msg=f"\n⟩—Delete task—⟨  {clock}\n")
        if len(all_task) == 0:
            laa()

        else:
            target = pix(all_task)
            all_task.pop(target - 1)
            save(all_task)
