
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import os
from os import listdir
from os.path import isfile, join
import pickle

# window
win = tk.Tk()
input_file = open("GUI_functions/submenu_new.bin", "rb")
this_machine = pickle.load(input_file)
input_file.close()
print(this_machine)
win.title(this_machinei[0]+"@"+this_machine[1])
# win.resizable(0,0)

path = os.path.dirname(os.path.realpath(__file__))

files = []
# r=root, d=directories, f = files

files = [f for f in listdir(path) if isfile(join(path, f))]


for f in files:
    if ".swp" in f:
        files.remove(f)
for i in files:
    print(i)

# modify adding label
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

# button click event
def clickMe():
    action.configure(text='Hello ' + name.get())

def click_configure_networks():
    action.configure(text='Hello ' + name.get())

# text box entry
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=40, textvariable=name)
nameEntered.grid(column=0, row=1)

# button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)

action = ttk.Button(win, text="Configure Networks", command=clickMe)
action.grid(column=1, row=1)

# action.configure(state='disabled')
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=12, row=10, sticky=tk.W, columnspan=3)
# drop down menu
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(4)

# checkbutton 1 (disabled)



# checkbutton 2 (unchecked)
chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=0, row=4, sticky=tk.W, columnspan=1)

# checkbutton 3 (enabled)
chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=1, row=4, sticky=tk.W, columnspan=3)

chVarAn = tk.IntVar()
check4 = tk.Checkbutton(win, text="GPU Enabled", variable=chVarAn)
check4.deselect()
check4.grid(column=2, row=4, sticky=tk.W, columnspan=3)

chVarAm = tk.IntVar()
check5 = tk.Checkbutton(win, text="GPU disabled", variable=chVarAm)
check5.deselect()
check5.grid(column=6, row=4, sticky=tk.W, columnspan=3)

chVarBn = tk.IntVar()
check6 = tk.Checkbutton(win, text="Network Enabled", variable=chVarBn)
check6.deselect()
check6.grid(column=9, row=4, sticky=tk.W, columnspan=3)

chVarBm = tk.IntVar()
check7 = tk.Checkbutton(win, text="Toolkit Enabled", variable=chVarBm)
check7.deselect()
check7.grid(column=11, row=4, sticky=tk.W, columnspan=3)


# GUI callback function
def checkCallback(*ignoredArgs):
    # only enable one checkbutton
    if chVarUn.get(): 
        check3.configure(state='disabled')
    else:       
        check3.configure(state='normal')
    if chVarEn.get(): 
        check2.configure(state='disabled')
    else:       
        check2.configure(state='normal')

chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())
chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())

def checkCallback2(*ignoredArgs):
    if chVarAn.get(): 
        check4.configure(state='normal')
        print("GPU Enabled up!")
    else:       
        print("GPU Enabled down!")
    if chVarAm.get(): 
        check5.configure(state='normal')
        print("GPU disabled up!")
    else:       
        print("GPU diableddown!")


chVarAm.trace('w', lambda unused3, unused4, unused5 : checkCallback2())
chVarAn.trace('w', lambda unused3, unused4, unused5 : checkCallback2())
# trace the state of the two checkbuttons


# scrolled text
scr = scrolledtext.ScrolledText(win, width=30, height=3, wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3)

# radio button global variables
colors = ['Python 3.6', 'Fortran', 'C', 'C++', 'NASM [64 bit]']

# Radiobutton callback function
def radCall():
    radSel=radVar.get()
    if   radSel == 0:
        print("Python 3.6")
        os.system("python3 select_py_GUI.py")
    elif radSel == 1:
        print("Fortran")
    elif radSel == 2:
        print("C")
    elif radSel == 3:
        print("C++")
    elif radSel == 4:
        print("NASM")
        os.system("python3 select_programs_GUI.py")

radVar = tk.IntVar()

# Next we are selecting a non-existing index value for radVar.
radVar.set(99)

# Now we are creating all ree Radiobutton widgets within one loop.
for col in range(5):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col + 10, row=1, sticky=tk.W)

# direct keyboard input to text box entry
nameEntered.focus()

win.mainloop()
