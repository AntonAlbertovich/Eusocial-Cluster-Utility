
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import os
from os import system
from os import listdir
from os.path import isfile, join
import pickle

win = tk.Tk()
input_file = open("GUI_functions/update.bin", "rb")
this_machine = list(pickle.load(input_file))
input_file.close()
win.title(str(this_machine[0])+"@"+this_machine[1])
# window
input_file.close()
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
py_Label = ttk.Label(win, text="Python")
py_Label.grid(column=2, row=1)

f90_Label = ttk.Label(win, text="Fortran")
f90_Label.grid(column=2, row=2)

c_Label = ttk.Label(win, text="C")
c_Label.grid(column=2, row=3)

cpp_Label = ttk.Label(win, text="C++")
cpp_Label.grid(column=2, row=4)

asm_Label = ttk.Label(win, text="Assembly")
asm_Label.grid(column=2, row=5)

cc_Label = ttk.Label(win, text="Number of Cores in Processor")
cc_Label.grid(column=2, row=6)

# button click event
def click_set_py():
    py_Label.configure(text='Python Executed with: $' + py_name.get())
    
    input_file= open("GUI_functions/Cluster_details.bin", "rb")
    machines = pickle.load(input_file)
    input_file.close()
    
    for i in range(len(machines)):
        print("ping")
        if this_machine[1] == machines[i][1]:
            print("!")
            machines[i][5][0] = py_name.get() 
            print(machines)
            output_file= open("GUI_functions/Cluster_details.bin", "wb")
            pickle.dump(machines, output_file)
            output_file.close()
            print(machines)
            break

def click_set_f90():
    f90_Label.configure(text='Fortran Executed with: $' + f90_name.get())
    input_file= open("GUI_functions/Cluster_details.bin", "rb")
    machines = pickle.load(input_file)
    input_file.close()
    
    for i in range(len(machines)):
        print("ping")
        if this_machine[1] == machines[i][1]:
            print("!")
            machines[i][5][1] = py_name.get() 
            print(machines)
            output_file= open("GUI_functions/Cluster_details.bin", "wb")
            pickle.dump(machines, output_file)
            output_file.close()
            print(machines)
            break

def click_set_c():
    c_Label.configure(text='C Executed with: $' + c_name.get())
    input_file= open("GUI_functions/Cluster_details.bin", "rb")
    machines = pickle.load(input_file)
    input_file.close()
    
    for i in range(len(machines)):
        print("ping")
        if this_machine[1] == machines[i][1]:
            print("!")
            machines[i][5][2] = c_name.get() 
            print(machines)
            output_file= open("GUI_functions/Cluster_details.bin", "wb")
            pickle.dump(machines, output_file)
            output_file.close()
            print(machines)
            break

def click_set_cpp():
    cpp_Label.configure(text='C++ Executed with: $' + cpp_name.get())
    input_file= open("GUI_functions/Cluster_details.bin", "rb")
    machines = pickle.load(input_file)
    input_file.close()
    
    for i in range(len(machines)):
        print("ping")
        if this_machine[1] == machines[i][1]:
            print("!")
            machines[i][5][3] = cpp_name.get() 
            print(machines)
            output_file= open("GUI_functions/Cluster_details.bin", "wb")
            pickle.dump(machines, output_file)
            output_file.close()
            print(machines)
            break


def click_set_asm():
    asm_Label.configure(text='Assembly Executed with: $' + asm_name.get())
    input_file= open("GUI_functions/Cluster_details.bin", "rb")
    machines = pickle.load(input_file)
    input_file.close()
    for i in range(len(machines)):
        print("ping")
        if this_machine[1] == machines[i][1]:
            print("!")
            machines[i][5][4] = asm_name.get() 
            print(machines)
            output_file= open("GUI_functions/Cluster_details.bin", "wb")
            pickle.dump(machines, output_file)
            output_file.close()
            print(machines)
            break

def click_set_cc():
    try:
        int_try = int(cc_name.get())
        if int_try > 0:
            cc_Label.configure(text='Accepted. There are: ' + cc_name.get() +'cores  on this machien.')
            input_file= open("GUI_functions/Cluster_details.bin", "rb")
            machines = pickle.load(input_file)
            input_file.close()
            for i in range(len(machines)):
                print("ping")
                if this_machine[1] == machines[i][1]:
                    print("Number")
                    machines[i][6] = int_try 
                    print(machines)
                    output_file= open("GUI_functions/Cluster_details.bin", "wb")
                    pickle.dump(machines, output_file)
                    output_file.close()
                    print(machines)
                    break

        else:
            cc_Label.configure(text='Input error, entry not accepted.')
    except ValueError:
        cc_Label.configure(text='Input error, entry not accepted.')
        

# text box entry
py_name = tk.StringVar()
py_nameEntered = ttk.Entry(win, width=12, textvariable=py_name)
py_nameEntered.grid(column=1, row=1)


f90_name = tk.StringVar()
f90_nameEntered = ttk.Entry(win, width=12, textvariable=f90_name)
f90_nameEntered.grid(column=1, row=2)

c_name = tk.StringVar()
c_nameEntered = ttk.Entry(win, width=12, textvariable=c_name)
c_nameEntered.grid(column=1, row=3)

cpp_name = tk.StringVar()
cpp_nameEntered = ttk.Entry(win, width=12, textvariable=cpp_name)
cpp_nameEntered.grid(column=1, row=4)

asm_name = tk.StringVar()
asm_nameEntered = ttk.Entry(win, width=12, textvariable=asm_name)
asm_nameEntered.grid(column=1, row=5)

cc_name = tk.StringVar()
cc_nameEntered = ttk.Entry(win, width=12, textvariable=cc_name)
cc_nameEntered.grid(column=1, row=6)


def click_configure_networks():
        print("Setting up Network...")
        import os
        os.system("python3 GUI_functions/select_networks.py")
        input_file = open("GUI_functions/update.bin", "rb")
        this_update = list(pickle.load(input_file))
        input_file.close()
        
        input_file= open("GUI_functions/Cluster_details.bin", "rb")
        machines = pickle.load(input_file)
        input_file.close()
        
        for i in range(len(machines)):
            if this_machine[1] == machines[i][1]:
                machines[i][2] = this_update 
                output_file= open("GUI_functions/Cluster_details.bin", "wb")
                pickle.dump(machines, output_file)
                output_file.close()
                break
        print(machines)


def click_configure_toolkits():
        print("Setting up toolkits...")
        import os
        os.system("python3 GUI_functions/select_toolkits.py")
        input_file = open("GUI_functions/update.bin", "rb")
        this_update = list(pickle.load(input_file))
        input_file.close()
        
        input_file= open("GUI_functions/Cluster_details.bin", "rb")
        machines = pickle.load(input_file)
        input_file.close()
        
        for i in range(len(machines)):
            print("ping")
            if this_machine[1] == machines[i][1]:
                machines[i][3] = this_update 
                output_file= open("GUI_functions/Cluster_details.bin", "wb")
                pickle.dump(machines, output_file)
                output_file.close()
                print(machines)
                break

def click_configure_avil():
        print("Setting time availablity...")
        import os
        os.system("python3 GUI_functions/select_hours.py")
        input_file = open("GUI_functions/update.bin", "rb")
        this_update = list(pickle.load(input_file))
        input_file.close()
        
        input_file= open("GUI_functions/Cluster_details.bin", "rb")
        machines = pickle.load(input_file)
        input_file.close()
        
        for i in range(len(machines)):
            print("ping")
            if this_machine[1] == machines[i][1]:
                machines[i][4] = this_update 
                output_file= open("GUI_functions/Cluster_details.bin", "wb")
                pickle.dump(machines, output_file)
                output_file.close()
                print(machines)
                break

def click_configure_dir():
        print("Setting up directory path...")
        import os
        os.system("python3 GUI_functions/select_networks.py")

def click_configure_time():
        print("Setting up time zone...")
        import os
        os.system("python3 GUI_functions/select_networks.py")


# text box entry

# button
click_set_py = ttk.Button(win, text="Set Python Program Execution Command", command=click_set_py, width=35)
click_set_py.grid(column=0, row=1)

click_set_f90 = ttk.Button(win, text="Set Fortran Program Execution Command", command=click_set_f90, width=35 )
click_set_f90.grid(column=0, row=2)

click_set_c = ttk.Button(win, text="Set C Program Execution Command", command=click_set_c, width=35)
click_set_c.grid(column=0, row=3)

click_set_cpp = ttk.Button(win, text="Set C++ Program Execution Command", command=click_set_cpp, width=35)
click_set_cpp.grid(column=0, row=4)

click_set_asm = ttk.Button(win, text="Set Assembly Program Execution Command", command=click_set_asm, width=35)
click_set_asm.grid(column=0, row=5)

click_set_cc = ttk.Button(win, text="Set Custom Core Count", command=click_set_cc, width=35)
click_set_cc.grid(column=0, row=6)





action_CD = ttk.Button(win, text="Configure Directory", command=click_configure_dir, width=25)
action_CD.grid(column=5, row=7)
action_CD.configure(state='disabled')
chVarDn = tk.IntVar()
check0 = tk.Checkbutton(win, text="This machine does NOT require custom ECU directory configuration.", variable=chVarDn)
check0.deselect()
check0.grid(column=0, row=7, sticky=tk.W, columnspan=3)
chVarDm = tk.IntVar()
check1 = tk.Checkbutton(win, text="This machine does require custom ECU directory configuration.", variable=chVarDm)
check1.deselect()
check1.grid(column=2, row=7, sticky=tk.W, columnspan=3)
def checkCallback0(*ignoredArgs):
    if chVarDm.get(): 
        check0.configure(state='disabled')
        action_CD.configure(state='normal')
    else:       
        check0.configure(state='normal')
        action_CD.configure(state='disabled')
    if chVarDn.get(): 
        check1.configure(state='disabled')
        action_CD.configure(state='disabled')
    else:       
        check1.configure(state='normal')
chVarDm.trace('w', lambda unused3, unused4, unused5 : checkCallback0())
chVarDn.trace('w', lambda unused3, unused4, unused5 : checkCallback0())



action_AT = ttk.Button(win, text="Configure Availability", command=click_configure_avil, width=25)
action_AT.grid(column=5, row=8)
action_AT.configure(state='disabled')
chVarEn = tk.IntVar()
check2 = tk.Checkbutton(win, text="This machine is available for cluster computation 24/7.", variable=chVarEn)
check2.deselect()
check2.grid(column=0, row=8, sticky=tk.W, columnspan=3)
chVarEm = tk.IntVar()
check3 = tk.Checkbutton(win, text="This machine is available only within a given time frame.", variable=chVarEm)
check3.deselect()
check3.grid(column=2, row=8, sticky=tk.W, columnspan=3)
def checkCallback1(*ignoredArgs):
    if chVarEm.get(): 
        check2.configure(state='disabled')
        action_AT.configure(state='normal')
    else:       
        check2.configure(state='normal')
        action_AT.configure(state='disabled')
    if chVarEn.get(): 
        check3.configure(state='disabled')
        action_AT.configure(state='disabled')
    else:       
        check3.configure(state='normal')
chVarEm.trace('w', lambda unused3, unused4, unused5 : checkCallback1())
chVarEn.trace('w', lambda unused3, unused4, unused5 : checkCallback1())




action_TZ = ttk.Button(win, text="Configure Timezone", command=click_configure_time, width=25)
action_TZ.grid(column=5, row=9)
action_TZ.configure(state='disabled')
chVarAn = tk.IntVar()
check4 = tk.Checkbutton(win, text="This machine is set to UTC time.", variable=chVarAn)
check4.deselect()
check4.grid(column=0, row=9, sticky=tk.W, columnspan=3)
chVarAm = tk.IntVar()
check5 = tk.Checkbutton(win, text="This machine is NOT set to UTC.", variable=chVarAm)
check5.deselect()
check5.grid(column=2, row=9, sticky=tk.W, columnspan=3)
def checkCallback2(*ignoredArgs):
    if chVarAm.get(): 
        check4.configure(state='disabled')
        action_TZ.configure(state='normal')
    else:       
        check4.configure(state='normal')
        action_TZ.configure(state='disabled')
    if chVarAn.get(): 
        check5.configure(state='disabled')
        action_TZ.configure(state='disabled')
        print("GPU disabled up!")
    else:       
        check5.configure(state='normal')
chVarAm.trace('w', lambda unused3, unused4, unused5 : checkCallback2())
chVarAn.trace('w', lambda unused3, unused4, unused5 : checkCallback2())


action_CN = ttk.Button(win, text="Configure Networks", command=click_configure_networks, width=25)
action_CN.grid(column=5, row=10)
action_CN.configure(state='disabled')
chVarBn = tk.IntVar()
check6 = tk.Checkbutton(win, text="This machine is connected to all other machines.", variable=chVarBn)
check6.deselect()
check6.grid(column=0, row=10, sticky=tk.W, columnspan=3)
chVarBm = tk.IntVar()
check7 = tk.Checkbutton(win, text="This machine requires a custom network configuration.", variable=chVarBm)
check7.deselect()
check7.grid(column=2, row=10, sticky=tk.W, columnspan=3)
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


action_CT = ttk.Button(win, text="Configure Toolkits", command=click_configure_toolkits, width=25)
action_CT.grid(column=5, row=11)
action_CT.configure(state='disabled')
chVarCn = tk.IntVar()
check8 = tk.Checkbutton(win, text="This machine has all necessary toolkits installed.", variable=chVarCn)
check8.deselect()
check8.grid(column=0, row=11, sticky=tk.W, columnspan=3)
chVarCm = tk.IntVar()
check9 = tk.Checkbutton(win, text="This machine requires a custom toolkit configuration.", variable=chVarCm)
check9.deselect()
check9.grid(column=2, row=11, sticky=tk.W, columnspan=3)
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

# Now we are creating all ree Radiobutton widgets within one loop.

os_0_Label = ttk.Label(win, text="Select an Operating System: ")
os_0_Label.grid(column=0, row=12)


os_distor= ['Ubuntu 18.04 [Desktop Edition]', 'CentOS 7 [Destop Edition]', 'CentOS 7 [Node/server Edition]', 'Unlisted Debian based OS', 'Unlisted Red Hat based OS']

def os_Call():
    coreSel=os_Var.get()
    if coreSel == 0:
        print("Ubuntu 18.04 [Desktop Edition]")
    elif coreSel == 1:
        print("CentOS 7 [Destop Edition]")
    elif coreSel == 2:
        print("CentOS 7 [Node/server Edition]")
    elif coreSel == 3:
        print("Unlisted Debian based OS")
    elif coreSel == 4:
        print("Unlisted Red Hat based OS")
    
    input_file= open("GUI_functions/Cluster_details.bin", "rb")
    machines = pickle.load(input_file)
    input_file.close()
    
    for i in range(len(machines)):
        print("ping")
        if this_machine[1] == machines[i][1]:
            print("!")
            machines[i][7] = os_distor[coreSel] 
            print(machines)
            output_file= open("GUI_functions/Cluster_details.bin", "wb")
            pickle.dump(machines, output_file)
            output_file.close()
            print(machines)
            break

os_Var = tk.IntVar()

# Next we are selecting a non-existing index value for radVar.
os_Var.set(99)

for os in range(5):
    cur_os = 'rad' + str(os)
    cur_os = tk.Radiobutton(win, text=os_distor[os], variable=os_Var, value=os, command=os_Call)
    cur_os.grid(column=0, row= os+13, sticky=tk.W)

def printMsg_kill():
    win.quit()

action_Q = ttk.Button(win, text="Save Cahnges", command=printMsg_kill, width=25)
action_Q.grid(column=0, row=19)

win.mainloop()
