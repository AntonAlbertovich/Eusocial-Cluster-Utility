
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import os
from os import listdir
from os.path import isfile, join

# window
win = tk.Tk()
win.title("Python GUI")
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

machines = ["machine 1", "machine 2", "machine 3", "machines"]


# button click event
def clickMe():
    action.configure(text='Hello ' + name.get())

def click_configure_networks():
        print("Setting up network...")

def click_configure_toolkits():
        print("Setting up toolkits...")

# text box entry
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)

action_CN = ttk.Button(win, text="Configure Networks", command=click_configure_networks)
action_CN.grid(column=8, row=5)
action_CN.configure(state='disabled')

action_CT = ttk.Button(win, text="Configure Toolkits", command=click_configure_toolkits)
action_CT.grid(column=8, row=6)
action_CT.configure(state='disabled')

# action.configure(state='disabled')
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=12, row=10, sticky=tk.W, columnspan=3)
# drop down menu
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)



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
check6 = tk.Checkbutton(win, text="This machine is connected to all other machines.", variable=chVarBn)
check6.deselect()
check6.grid(column=0, row=5, sticky=tk.W, columnspan=3)

chVarBm = tk.IntVar()
check7 = tk.Checkbutton(win, text="This machine requires a custom network configuration.", variable=chVarBm)
check7.deselect()
check7.grid(column=3, row=5, sticky=tk.W, columnspan=3)


chVarCn = tk.IntVar()
check8 = tk.Checkbutton(win, text="This machine has all necessary toolkits installed.", variable=chVarCn)
check8.deselect()
check8.grid(column=0, row=6, sticky=tk.W, columnspan=3)

chVarCm = tk.IntVar()
check9 = tk.Checkbutton(win, text="This machine requires a custom toolkit configuration.", variable=chVarCm)
check9.deselect()
check9.grid(column=3, row=6, sticky=tk.W, columnspan=3)


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
    if chVarAm.get(): 
        check4.configure(state='disabled')
        print("GPU Enabled up!")
    else:       
        check4.configure(state='normal')
        print("GPU Enabled down!")
    if chVarAn.get(): 
        check5.configure(state='disabled')
        print("GPU disabled up!")
    else:       
        check5.configure(state='normal')
        print("GPU diableddown!")


chVarAm.trace('w', lambda unused3, unused4, unused5 : checkCallback2())
chVarAn.trace('w', lambda unused3, unused4, unused5 : checkCallback2())

def checkCallback3(*ignoredArgs):
    if chVarBm.get(): 
        check6.configure(state='disabled')
        action_CN.configure(state='normal')
    else:       
        check6.configure(state='normal')
        action_CN.configure(state='disabled')
    if chVarBn.get(): 
        check7.configure(state='disabled')
        action_CN.configure(state='disabled')
        print("GPU disabled up!")
    else:       
        check7.configure(state='normal')


chVarBm.trace('w', lambda unused3, unused4, unused5 : checkCallback3())
chVarBn.trace('w', lambda unused3, unused4, unused5 : checkCallback3())

def checkCallback4(*ignoredArgs):
    if chVarCm.get(): 
        check8.configure(state='disabled')
        action_CT.configure(state='normal')
    else:       
        check8.configure(state='normal')
        action_CT.configure(state='disabled')
    if chVarCn.get(): 
        check9.configure(state='disabled')
        action_CT.configure(state='disabled')
    else:       
        check9.configure(state='normal')


chVarCm.trace('w', lambda unused3, unused4, unused5 : checkCallback4())
chVarCn.trace('w', lambda unused3, unused4, unused5 : checkCallback4())

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
    curRad.grid(column=col + 5, row=1, sticky=tk.W)



core_count = ['4 Cores', '6 Cores', '8 Cores', '10 Cores', '12 Cores', '14 Cores', '16 Cores', '18 Cores', 'Custom Core Count']

def coreCall():
    coreSel=coreVar.get()
    if coreSel == 0:
        print("4")
    elif coreSel == 1:
        print("6")
    elif coreSel == 2:
        print("8")
    elif coreSel == 3:
        print("10")
    elif coreSel == 4:
        print("12")
    elif coreSel == 5:
        print("14")
    elif coreSel == 6:
        print("16")
    elif coreSel == 7:
        print("18")
    elif coreSel == 8:
        print("Custom")


coreVar = tk.IntVar()

# Next we are selecting a non-existing index value for radVar.
radVar.set(99)

for core in range(9):
    cur_core = 'rad' + str(core)
    cur_core = tk.Radiobutton(win, text=core_count[core], variable=coreVar, value=core, command=coreCall)
    cur_core.grid(column=core + 0, row=8, sticky=tk.W)

win.mainloop()
