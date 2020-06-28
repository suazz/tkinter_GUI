from tkinter import ttk
from tkinter import *
global total

y = 0
n = ttk.Notebook()
f1 = ttk.Frame(n)
f2 = ttk.Frame(n)
f3 = ttk.Frame(n)
f4 = ttk.Frame(n)
f5 = ttk.Frame(n)
f6 = ttk.Frame(n)
f7 = ttk.Frame(n)

window = ttk.Frame(n)

# new Tabs
def main(x):
    global total
    n.add(f1, text="NOT")
    n.add(f2, text="OR")
    n.add(f3, text="AND")
    n.add(f4, text="NOT OR")
    n.add(f5, text="NOT AND")
    n.add(f6, text="!=")
    n.add(f7, text="==")

    total = ttk.Label(window, text="0")

# not
    Label(f1, text="not False").grid(row=2, column=2)
    Button(f1, text="True", command=correct).grid(row=3, column=2)
    Button(f1, text="False", command=incorrect).grid(row=3, column=3)

    Label(f1, text="not True").grid(row=4, column=2)
    Button(f1, text="True", command=incorrect).grid(row=5, column=2)
    Button(f1, text="False", command=correct).grid(row=5, column=3)
# or
    Label(f2, text="True or False").grid(row=2, column=2)
    Button(f2, text="True", command=correct2).grid(row=3, column=2)
    Button(f2, text="False", command=incorrect2).grid(row=3, column=3)

    Label(f2, text="True or True").grid(row=4, column=2)
    Button(f2, text="True", command=correct2).grid(row=5, column=2)
    Button(f2, text="False", command=incorrect2).grid(row=5, column=3)

    Label(f2, text="False or True").grid(row=6, column=2)
    Button(f2, text="True", command=correct2).grid(row=7, column=2)
    Button(f2, text="False", command=incorrect2).grid(row=7, column=3)

    Label(f2, text="False or False").grid(row=8, column=2)
    Button(f2, text="True", command=incorrect2).grid(row=9, column=2)
    Button(f2, text="False", command=correct2).grid(row=9, column=3)
# and
    Label(f3, text="True and False").grid(row=2, column=2)
    Button(f3, text="True", command=incorrect3).grid(row=3, column=2)
    Button(f3, text="False", command=correct3).grid(row=3, column=3)

    Label(f3, text="True and True").grid(row=4, column=2)
    Button(f3, text="True", command=correct3).grid(row=5, column=2)
    Button(f3, text="False", command=incorrect3).grid(row=5, column=3)

    Label(f3, text="False and True").grid(row=6, column=2)
    Button(f3, text="True", command=incorrect3).grid(row=7, column=2)
    Button(f3, text="False", command=correct3).grid(row=7, column=3)

    Label(f3, text="False and False").grid(row=8, column=2)
    Button(f3, text="True", command=incorrect3).grid(row=9, column=2)
    Button(f3, text="False", command=correct3).grid(row=9, column=3)
# not or
    Label(f4, text="not (True or False)").grid(row=2, column=2)
    Button(f4, text="True", command=incorrect4).grid(row=3, column=2)
    Button(f4, text="False", command=correct4).grid(row=3, column=3)

    Label(f4, text="not (True or True)").grid(row=4, column=2)
    Button(f4, text="True", command=incorrect4).grid(row=5, column=2)
    Button(f4, text="False", command=correct4).grid(row=5, column=3)

    Label(f4, text="not (False or True)").grid(row=6, column=2)
    Button(f4, text="True", command=incorrect4).grid(row=7, column=2)
    Button(f4, text="False", command=correct4).grid(row=7, column=3)

    Label(f4, text="not (False or False)").grid(row=8, column=2)
    Button(f4, text="True", command=correct4).grid(row=9, column=2)
    Button(f4, text="False", command=incorrect4).grid(row=9, column=3)
# not and
    Label(f5, text="not (True and False)").grid(row=2, column=2)
    Button(f5, text="True", command=correct5).grid(row=3, column=2)
    Button(f5, text="False", command=incorrect5).grid(row=3, column=3)

    Label(f5, text="not (True and True)").grid(row=4, column=2)
    Button(f5, text="True", command=incorrect5).grid(row=5, column=2)
    Button(f5, text="False", command=correct5).grid(row=5, column=3)

    Label(f5, text="not (False and True)").grid(row=6, column=2)
    Button(f5, text="True", command=correct5).grid(row=7, column=2)
    Button(f5, text="False", command=incorrect5).grid(row=7, column=3)

    Label(f5, text="not (True and False)").grid(row=8, column=2)
    Button(f5, text="True", command=correct5).grid(row=9, column=2)
    Button(f5, text="False", command=incorrect5).grid(row=9, column=3)
# !=
    Label(f6, text="1 ! = 0").grid(row=2, column=2)
    Button(f6, text="True", command=correct6).grid(row=3, column=2)
    Button(f6, text="False", command=incorrect6).grid(row=3, column=3)

    Label(f6, text="1 ! = 1").grid(row=4, column=2)
    Button(f6, text="True", command=incorrect6).grid(row=5, column=2)
    Button(f6, text="False", command=correct6).grid(row=5, column=3)

    Label(f6, text="0 ! = 1").grid(row=6, column=2)
    Button(f6, text="True", command=correct6).grid(row=7, column=2)
    Button(f6, text="False", command=incorrect6).grid(row=7, column=3)

    Label(f6, text="0 ! = 0").grid(row=8, column=2)
    Button(f6, text="True", command=incorrect6).grid(row=9, column=2)
    Button(f6, text="False", command=correct6).grid(row=9, column=3)
# ==
    Label(f7, text="1 == 0").grid(row=2, column=2)
    Button(f7, text="True", command=incorrect7).grid(row=3, column=2)
    Button(f7, text="False", command=correct7).grid(row=3, column=3)

    Label(f7, text="1 == 1").grid(row=4, column=2)
    Button(f7, text="True", command=correct7).grid(row=5, column=2)
    Button(f7, text="False", command=incorrect7).grid(row=5, column=3)

    Label(f7, text="0 == 1").grid(row=6, column=2)
    Button(f7, text="True", command=incorrect7).grid(row=7, column=2)
    Button(f7, text="False", command=correct7).grid(row=7, column=3)

    Label(f7, text="0 == 0").grid(row=8, column=2)
    Button(f7, text="True", command=correct7).grid(row=9, column=2)
    Button(f7, text="False", command=incorrect7).grid(row=9, column=3)
    return total


def correct():
    global total
    Label(f1, text="  CORRECT  ", fg="white", bg="green").grid(row=2, column=4)
    counter()


def incorrect():
    Label(f1, text="INCORRECT", fg="white", bg="red").grid(row=2, column=4)
    counter()


def correct2():
    global total
    Label(f2, text="  CORRECT  ", fg="white", bg="green").grid(row=2, column=4)
    counter()


def incorrect2():
    Label(f2, text="INCORRECT", fg="white", bg="red").grid(row=2, column=4)
    counter()


def correct3():
    global total
    Label(f3, text="  CORRECT  ", fg="white", bg="green").grid(row=2, column=4)
    counter()


def incorrect3():
    Label(f3, text="INCORRECT", fg="white", bg="red").grid(row=2, column=4)
    counter()


def correct4():
    global total
    Label(f4, text="  CORRECT  ", fg="white", bg="green").grid(row=2, column=4)
    counter()


def incorrect4():
    Label(f4, text="INCORRECT", fg="white", bg="red").grid(row=2, column=4)
    counter()


def correct5():
    global total
    Label(f5, text="  CORRECT  ", fg="white", bg="green").grid(row=2, column=4)
    counter()


def incorrect5():
    Label(f5, text="INCORRECT", fg="white", bg="red").grid(row=2, column=4)
    counter()


def correct6():
    global total
    Label(f6, text="  CORRECT  ", fg="white", bg="green").grid(row=2, column=4)
    counter()


def incorrect6():
    Label(f6, text="INCORRECT", fg="white", bg="red").grid(row=2, column=4)
    counter()


def correct7():
    global total
    Label(f7, text="  CORRECT  ", fg="white", bg="green").grid(row=2, column=4)
    counter()


def incorrect7():
    Label(f7, text="INCORRECT", fg="white", bg="red").grid(row=2, column=4)
    counter()


def counter():
    global total
    total['text'] = str(int(total['text']) + 1)


main(y)


n.pack()

n.mainloop()
