#!/usr/bin/env python3

from pathlib import Path
import argparse
import json
import time
import sys
import os


loc = Path.home() / ".dotask_notes.json"    # Lokasi catatan
if not loc.exists():
    loc.touch()
    loc.write_text("[]")

trash = Path.home() / ".dotask_trash.json"    # ← Tempat buang
if not trash.exists():                          # tugas yang dihapus
    trash.touch()
    trash.write_text("[]")


def tasks(dft, msg):    # print daftar tugas kalo ada
    print(msg)
    for no, tugas in enumerate(dft, 1):
        for nama, status in tugas.items():
            print(f"[{no}] {nama} ~> {status}")
    if len(dft) > 0:
        print("")
    else:
        return


def pix(task):      # Ambil input angka dari user
    while True:
        slct = input("Select number: ")
        if slct == "all":
            return slct
        elif not slct.isdigit():
            pass
        elif int(slct) > 0 and int(slct) <= len(task):
            return slct
            break
        print(outside)


def notes(lokasi):       # Baca
    try:
        with open(lokasi, "r") as f:
            task = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        task = []
    return task


def save(lokasi, target, yes=False):        # Tulis
    if yes:
        with open(lokasi, "w") as f:
            json.dump(target, f, indent=2)
        return True

    sure = input("You sure? (y/n): ")   # Jika nggak pake -y masuk sini
    if sure.lower() == "y":
        with open(lokasi, "w") as f:
            json.dump(target, f, indent=2)
        return True


def throw(task, select_all=False):     # Lempar tugas yg dibuang
    if select_all:                     # ke tempat sampah
        for i in task:
            rubbish.append({time.strftime("%d/%m/%y"): i})
    else:
        for i in task:      # masuk sini jika cuma pilih 1 yg dihapus
            k = list(task.keys())[0]
            v = list(task.values())[0]
            rubbish.append({time.strftime("%d/%m/%y"): {k: v}})

    if len(rubbish) >= 50:     # Bersih bersih sampah
        rubbish.clear()


def end():      # Tergantung user nambahin argument show ato nggak
    if args.show:
        pass
    else:
        sys.exit()


def resik():    # Bersih bersih terminal (malas ketik)
    os.system("cls" if os.name == "nt" else "clear")


opt = {
    "[1]": "To-Do-List",
    "[2]": "Add task",
    "[3]": "Change task",       # Daftar pilihan di mode interaktif
    "[4]": "Delete task",
    "[0]": "Exit"
    }
outside = ("Enter the available number!")   # Cuma males ketik aja ini

# flag
parser = argparse.ArgumentParser(description="to do list simple")
groups = parser.add_mutually_exclusive_group()

# argument utama
groups.add_argument(
    "--add", action="store_true",
    help="example: dotask --add --name 'dicintai olehnya' "
         "--stat 'di dalam mimpiku' -y")
groups.add_argument(
    "--delete", type=int, metavar="",
    help="example: dotask --delete 1 -y")
groups.add_argument(
    "--change", type=int, metavar="",
    help="example: dotask --change 2 --name 'RRQ Samsudin' "
         "--stat 'Jago sulap' -y")
groups.add_argument(
    "--finished", type=int, metavar="",
    help="example: dotask --finished 3 -y")
groups.add_argument(
    "--undo", type=str, metavar="",
    help="example: dotask --undo '01/07/25' -y")


# argument pendukung yang diperlukan beberapa argument utama
parser.add_argument(
    "--name", type=str, metavar="",
    help="use to name task")
parser.add_argument(
    "--stat", type=str, metavar="",
    help="use to task status")


# argument pendukung argument utama, tapi opsional
parser.add_argument(
    "--select-all", "-A", action="store_true",
    help="use to select all when deleting")
parser.add_argument(
    "--yes", "-y", action="store_true",
    help="use to skip approval")


# argument yang bisa dijalankan tanpa argument tambahan
parser.add_argument(
    "--show", action="store_true",
    help="use to display all tasks")
groups.add_argument(
    "--find", type=str, metavar="",
    help="example: dotask --find 'RRQ Samsudin'")
groups.add_argument(
    "--version", "-V", action="store_true",
    help="use to check version dotask")


args = parser.parse_args()
if args.finished is not None:
    i = args.finished - 1
    all_task = notes(loc)
    if args.finished > 0 and len(all_task) >= args.finished:
        k = list(all_task[i].keys())[0]     # Ambil keys dari dictonary
        all_task[i] = {k: "Finished"}
        y = save(loc, all_task, yes=args.yes)
        if y:
            print("dotask: mark successful..")      # Jika y True
        else:
            print("dotask: mark cancelled..")
    else:
        print("dotask: invalid index or empty task, mark failed..")
    end()

elif args.add:
    all_task = notes(loc)
    if not args.name.strip() or not args.stat.strip():
        print("dotask: the task name or status cannot be empty!!")
        sys.exit()
    elif args.name and args.stat:
        all_task.append({args.name: args.stat})
        y = save(loc, all_task, yes=args.yes)
        if y:
            print("dotask: add success..")
        else:
            print("dotask: addition cancelled..")
    else:
        print("dotask: addition failed..")
    end()

elif args.change is not None:
    i = args.change - 1
    all_task = notes(loc)
    if args.change > 0 and len(all_task) >= args.change:
        if args.name and not args.stat:
            v = list(all_task[i].values())[0]   # Ambil Value dari dict
            all_task[i] = {args.name: v}
            y = save(loc, all_task, yes=args.yes)
            if y:
                print("dotask: name changed successfully..")
            else:
                print("dotask: changes canceled..")
        elif args.stat and not args.name:
            k = list(all_task[i].keys())[0]     # Ambil keys dari dict
            all_task[i] = {k: args.stat}
            y = save(loc, all_task, yes=args.yes)
            if y:
                print("dotask: status changed successfully..")
            else:
                print("dotask: changes canceled..")
        elif args.name and args.stat:
            all_task[i] = {args.name: args.stat}    # Rubah keys
            y = save(loc, all_task, yes=args.yes)   # dan values
            if y:
                print("dotask: name and status change successful..")
            else:
                print("dotask: changes canceled..")
    else:
        print("dotask: invalid index or empty task, change failed..")
    end()

elif args.delete is not None:
    i = args.delete - 1
    all_task = notes(loc)
    rubbish = notes(trash)
    if args.select_all:    # Masuk blok sini kalo user pake argumentnya
        throw(all_task, select_all=True)
        all_task.clear()
        y = save(loc, all_task, yes=args.yes)
        if y:
            save(trash, rubbish, yes=True)
            print("dotask: all tasks successfully deleted..")
        else:
            print("dotask: deletion canceled..")
    else:       # Masuk sini kalo user cuma input angka
        if args.delete > 0 and len(all_task) >= args.delete:
            throw(all_task[i])
            all_task.pop(i)
            y = save(loc, all_task, yes=args.yes)   # kalo user pilih
            if y:                                   # y masuk blok ini
                save(trash, rubbish, yes=True)
                print("dotask: delete successfully..")
            else:
                print("dotask: deletion canceled..")
        else:
            print("dotask: invalid index or empty task, "
                  "delete failed..")
    end()

elif args.undo:
    all_task = notes(loc)
    rubbish = notes(trash)
    found = 0
    for task in rubbish:    # Bongkar satu persatu isi List
        if args.undo in task:
            k = list(task[args.undo].keys())[0]
            v = list(task[args.undo].values())[0]
            all_task.append({k: v})
            task.pop(args.undo)
            found += 1

    if not found:   # Kalo pas bongkar nggak nemu apa apa, masuk sini
        print(f"dotask: task deleted on {args.undo} not found..")
    else:   # Kalo pas bongkar nemu, masuk sini
        print(f"dotask: found {found} deleted tasks on {args.undo}")
        y = save(loc, all_task, yes=args.yes)
        if y:
            rubbish = [x for x in rubbish if x]   # ← filter hanya isi
            save(trash, rubbish, yes=True)          # yg bernilai true
            print("dotask: tasks successfully recovered..")
        else:
            print("dotask: recovery cancelled..")
    end()

elif args.find:
    all_task = notes(loc)
    results = []
    for i, task in enumerate(all_task, 1):
        k = list(task.keys())[0]
        v = list(task.values())[0]
        if args.find.lower() in k.lower():      # Cari dengan convert
            results.append(f"[{i}] {k} ~> {v}") # ke huruf kecil semua

    if results:
        print("\n⟩—Results found—⟨\n")
        print("\n".join(results))
    else:
        print("dotask: results not found..")
    sys.exit()

if args.show:
    all_task = notes(loc)
    if len(all_task) > 0:   # Jika isi tidak kosong masuk blok ini
        tasks(all_task, msg=f"\n⟩—To do list—⟨\n")
    else:   # Kalo kosong masuk sini
        print("dotask: empty..")
    sys.exit()

if args.version:
    print("developed by Fenrix\n"
          "DoTask Version 02.29.50")
    sys.exit()


# interactive mode
while True:     # Biar user nggak langsung dipentalin keluar
    resik()
    clock = time.strftime("[%H:%M]")
    print(f"\n⟩—Option—⟨  {clock}\n")
    for opsi, isi in opt.items():
        print(f"{opsi} {isi}")


    while True:     # Hqnya terima input yg tersedia
        user = input("\nSelect option: ").strip()
        if user in["1", "2", "3", "4"]:
            break

        elif user == "0":
            print(
                 "\nVersion 02.29.50"   # versi nggak pasti
                 "\nBy Fenrix"
            )
            sys.exit()
        print(outside)


    if user == "1":   # Daftar tugas dan tandai selesai
        resik()
        all_task = notes(loc)
        tasks(all_task, msg=f"\n⟩—To do list—⟨  {clock}\n")
        while True:
            rsp = input("What tasks have you just completed? "
                        "(N)one: ").strip()
            if rsp.lower() == "n":  # Kembali ke halaman awal
                break               # kalo nggka jadi nandain tugas

            elif not rsp.isdigit():
                print(outside)

            elif int(rsp) > len(all_task) or int(rsp) <= 0:
                print(outside)

            else:
                i = int(rsp) - 1
                k = list(all_task[i].keys())[0]
                all_task[i] = {k: "Finished"}
                save(loc, all_task)
                break


    elif user == "2":   # Tambah tugas
        resik()
        all_task = notes(loc)   # Buka file catatan
        tasks(all_task, msg=f"\n⟩—Add task—⟨  {clock}\n")
        while True:
            task = input("Task name: ").strip()
            stat = input("Task stat: ").strip()
            if not task or not stat:
                print("the task name or status cannot be empty!!")
            else:
                all_task.append({task: stat})   # Tambah isi List
                save(loc, all_task)     # Simpan
                break   # Akhiri loop


    elif user == "3":   # Rubah tugas
        resik()
        all_task = notes(loc)   # Buka file catatan
        tasks(all_task, msg=f"\n⟩—Change task—⟨  {clock}\n")

        if len(all_task) == 0:      # Kalo isi kosong
            print("[!] Empty!")
            press = input("\nPress anywhere: ")

        else:
            while True:
                target = pix(all_task)
                if target.isdigit():
                    break
                print("Option not allowed!!\n")
            i = int(target) - 1
            while True:
                task = input("Task name: ").strip()
                stat = input("Task stat: ").strip()
                if not task or not stat:
                    print("the task name or status cannot be empty!!")
                else:
                    all_task[i] = {task: stat}
                    save(loc, all_task)     # Simpan perubahan
                    break   # Akhiri loop


    elif user == "4":   # Hapus tugas
        resik()
        all_task = notes(loc)
        rubbish = notes(trash)      # Buka file tempat samaph
        tasks(all_task, msg=f"\n⟩—Delete task—⟨  {clock}\n")

        if len(all_task) == 0:      # Kalo isi kosong
            print("[!] Empty!")
            press = input("\nPress anywhere: ")

        else:
            target = pix(all_task)
            if target == "all":     # Pilih semua
                throw(all_task, select_all=True)    # Jadikan ke true dl
                all_task.clear()
                y = save(loc, all_task)
                if y:
                    save(trash, rubbish, yes=True)
            else:
                i = int(target) - 1
                throw(all_task[i])
                all_task.pop(i)
                y = save(loc, all_task) # Jika disini user pilih y
                if y:                   # otomatis masuk blok ini
                    save(trash, rubbish, yes=True)
