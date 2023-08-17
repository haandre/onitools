from names import get_full_name
from subprocess import Popen, PIPE
from tkinter import Tk
from tkinter import ttk


labels = {}


def generate_name(gender: str = "female") -> str:
    return get_full_name(gender=gender)


def copy_string_to_clipboard(data: str):
    Popen(('clip'), stdin=PIPE).communicate(data.encode())


def get_name(gender: str="female"):
    name = generate_name(gender=gender)
    copy_string_to_clipboard(name)
    labels[gender].configure(text=name)


def male():
    get_name("male")

def female():
    get_name()


def main():
    root = Tk()
    # root.geometry("200x100")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Names 2 Cilpboard!").grid(column=0, row=0, columnspan=2)
    labels["female"] = ttk.Label(frm, text=" ")
    labels["female"].grid(column=1, row=1)
    labels["male"] = ttk.Label(frm, text=" ")
    labels["male"].grid(column=1, row=2)
    ttk.Button(frm, text="Female", command=female).grid(column=0, row=1)
    ttk.Button(frm, text="Male", command=male).grid(column=0, row=2)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3)
    ttk.Label(frm, text=" " * 40).grid(column=1, row=3)
    root.mainloop()


if __name__ == "__main__":
    main()
