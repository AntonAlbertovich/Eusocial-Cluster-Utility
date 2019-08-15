import tkinter as tk

from tkinter import *
from os import walk
import os
from os import listdir
from os.path import isfile, join
import pickle

# This script simply builds the sub-menu for all assembly programs.
# A scrollable window is generated
# When a program is selected then the universal depenecies sub-menu is open via select_depend.py
# Once the edits have been made to the universal depenecies sub-menu the user may update the task detials data structure via clicking the button: "Save and Update Settings"

class ScrollFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent) 

    
        self.canvas = tk.Canvas(self, borderwidth=0)          
        self.viewPort = tk.Frame(self.canvas)                     
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview) 
        self.canvas.configure(yscrollcommand=self.vsb.set)                          
        self.vsb.pack(side="right", fill="y")                                       
        self.canvas.pack(side="left", fill="both", expand=True)                     
        self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)           

    def onFrameConfigure(self, event):                                              
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))  



class menu_frame(tk.Frame):

    def __init__(self, root, this_machine):
        def click_set_cc():
            # This allows the user to enter the number of CPU cores of a given machine.
            print(cc_nameEntered.get())

            try:
                int_try = int(cc_nameEntered.get())
                print(int_try)
                if int_try > 0:
                    tk.Label(self.scrollFrame.viewPort, text='Accepted. There are: ' + cc_nameEntered.get() +' cores  on this machien.').grid(column=2, row=6)
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
                    tk.Label(self.scrollFrame.viewPort, text="Error").grid(column=2, row=6)
            except ValueError:
                tk.Label(self.scrollFrame.viewPort, text="Errorwwwwww").grid(column=2, row=6)
    
        def click_set_py():
            # This allows the user to enter a default execution command for all python scripts.
            tk.Label(self.scrollFrame.viewPort, text='Python Executed with: $' + py_nameEntered.get()).grid(column=2, row=1)
            input_file= open("GUI_functions/Cluster_details.bin", "rb")
            machines = pickle.load(input_file)
            input_file.close()

            for i in range(len(machines)):
                if this_machine[1] == machines[i][1]:
                    machines[i][5][0] = py_nameEntered.get()
                    output_file= open("GUI_functions/Cluster_details.bin", "wb")
                    pickle.dump(machines, output_file)
                    output_file.close()
                    break


        def click_set_c():
            # This allows the user to enter a default execution command for all C scripts.
            tk.Label(self.scrollFrame.viewPort, text='C Executed with: $' + c_nameEntered.get()).grid(column=2, row=3)
            input_file= open("GUI_functions/Cluster_details.bin", "rb")
            machines = pickle.load(input_file)
            input_file.close()

            for i in range(len(machines)):
                if this_machine[1] == machines[i][1]:
                    machines[i][5][2] = c_nameEntered.get()
                    output_file= open("GUI_functions/Cluster_details.bin", "wb")
                    pickle.dump(machines, output_file)
                    output_file.close()
                    break

        def click_set_asm():
            # This allows the user to enter a default execution command for all assembly scripts.
            tk.Label(self.scrollFrame.viewPort, text='ASM Executed with: $' + asm_nameEntered.get()).grid(column=2, row=5)
            input_file= open("GUI_functions/Cluster_details.bin", "rb")
            machines = pickle.load(input_file)
            input_file.close()
            for i in range(len(machines)):
                print("ping")
                if this_machine[1] == machines[i][1]:
                    print("!")
                    machines[i][5][4] = asm_nameEntered.get()
                    print(machines)
                    output_file= open("GUI_functions/Cluster_details.bin", "wb")
                    pickle.dump(machines, output_file)
                    output_file.close()
                    print(machines)
                    break



        def click_set_f90():
            # This allows the user to enter a default execution command for all fortran scripts.
            tk.Label(self.scrollFrame.viewPort, text='Fortran Executed with: $' + f90_nameEntered.get()).grid(column=2, row=2)
            input_file= open("GUI_functions/Cluster_details.bin", "rb")
            machines = pickle.load(input_file)
            input_file.close()

            for i in range(len(machines)):
                if this_machine[1] == machines[i][1]:
                    machines[i][5][1] = f90_nameEntered.get()
                    output_file= open("GUI_functions/Cluster_details.bin", "wb")
                    pickle.dump(machines, output_file)
                    output_file.close()
                    break



        def click_set_cpp():
            # This allows the user to enter a default execution command for all C++ scripts.
            tk.Label(self.scrollFrame.viewPort, text='C++ Executed with: $' + cpp_nameEntered.get()).grid(column=2, row=4)
            input_file= open("GUI_functions/Cluster_details.bin", "rb")
            machines = pickle.load(input_file)
            input_file.close()

            for i in range(len(machines)):

                if this_machine[1] == machines[i][1]:
                    machines[i][5][3] = cpp_nameEntered.get()
                    output_file= open("GUI_functions/Cluster_details.bin", "wb")
                    pickle.dump(machines, output_file)
                    output_file.close()
                    break


        def click_configure_dir():
                # This function opens the window for entering a custom directory for a machine in a given cluster.
                # As of 7/05/2019 this feature has not been fully integrated yet.
                print("Setting up directory path...")



        tk.Frame.__init__(self, root)
        self.scrollFrame = ScrollFrame(self) # add a new scrollable frame.


        self.scrollFrame.pack(side="top", fill="both", expand=True)
    


        tk.Label(self.scrollFrame.viewPort, text="Python").grid(column=2, row=1)
        tk.Label(self.scrollFrame.viewPort, text="Fortran").grid(column=2, row=2)
        tk.Label(self.scrollFrame.viewPort, text="C").grid(column=2, row=3)
        tk.Label(self.scrollFrame.viewPort, text="C++").grid(column=2, row=4)
        tk.Label(self.scrollFrame.viewPort, text="Assembly").grid(column=2, row=5)
        tk.Label(self.scrollFrame.viewPort, text="Number of Cores in Processor").grid(column=2, row=6)

        py_name = tk.StringVar()
        py_nameEntered = tk.Entry(self.scrollFrame.viewPort, width=12, textvariable=py_name)
        py_nameEntered.grid(column=1, row=1)

        f90_name = tk.StringVar()
        f90_nameEntered = tk.Entry(self.scrollFrame.viewPort, width=12, textvariable=f90_name)
        f90_nameEntered.grid(column=1, row=2)

        c_name = tk.StringVar()
        c_nameEntered = tk.Entry(self.scrollFrame.viewPort, width=12, textvariable=c_name)
        c_nameEntered.grid(column=1, row=3)

        cpp_name = tk.StringVar()
        cpp_nameEntered = tk.Entry(self.scrollFrame.viewPort, width=12, textvariable=cpp_name)
        cpp_nameEntered.grid(column=1, row=4)

        asm_name = tk.StringVar()
        asm_nameEntered = tk.Entry(self.scrollFrame.viewPort, width=12, textvariable=asm_name)
        asm_nameEntered.grid(column=1, row=5)

        cc_name = tk.StringVar()
        cc_nameEntered = tk.Entry(self.scrollFrame.viewPort, width=12, textvariable=cc_name)
        cc_nameEntered.grid(column=1, row=6)

        click_set_py = tk.Button(self.scrollFrame.viewPort, text="Set Python Program Execution Command", command=click_set_py, width=35)
        click_set_py.grid(column=0, row=1)

        click_set_f90 = tk.Button(self.scrollFrame.viewPort, text="Set Fortran Program Execution Command", command=click_set_f90, width=35 )
        click_set_f90.grid(column=0, row=2)

        click_set_c = tk.Button(self.scrollFrame.viewPort, text="Set C Program Execution Command", command=click_set_c, width=35)
        click_set_c.grid(column=0, row=3)

        click_set_cpp = tk.Button(self.scrollFrame.viewPort, text="Set C++ Program Execution Command", command=click_set_cpp, width=35)
        click_set_cpp.grid(column=0, row=4)

        click_set_asm = tk.Button(self.scrollFrame.viewPort, text="Set Assembly Program Execution Command", command=click_set_asm, width=35)
        click_set_asm.grid(column=0, row=5)

        click_set_cc = tk.Button(self.scrollFrame.viewPort, text="Set Custom Core Count", command=click_set_cc, width=35)
        click_set_cc.grid(column=0, row=6)


        def checkCallback0():
            print("ping")
            check0.select()
            check1.deselect()
            action_CD = tk.Button(self.scrollFrame.viewPort, text="Configure Directory", command=click_configure_dir, width=25)
            action_CD.grid(column=5, row=7)
            action_CD.configure(state='disabled')
        def checkCallback1():
            print("ring")
            check1.select()
            check0.deselect()
            action_CD = tk.Button(self.scrollFrame.viewPort, text="Configure Directory", command=click_configure_dir, width=25)
            action_CD.grid(column=5, row=7)
        chVarDn = tk.IntVar()
        check0 = tk.Checkbutton(self.scrollFrame.viewPort, text="This machine does NOT require custom directory configuration.", command=checkCallback0, variable=chVarDn)
        check0.deselect()
        check0.grid(column=0, row=7, sticky=tk.W, columnspan=3)
        chVarDm = tk.IntVar()
        check1 = tk.Checkbutton(self.scrollFrame.viewPort, text="This machine does require custom ECU directory configuration.", command=checkCallback1,  variable=chVarDm)
        check1.deselect()
        check1.grid(column=2, row=7, sticky=tk.W, columnspan=3)

        def checkCallback2():
            print("ping")
            check2.select()
            check3.deselect()
            action_CD = tk.Button(self.scrollFrame.viewPort, text="Configure Directory", command=click_configure_dir, width=25)
            action_CD.grid(column=5, row=8)
            action_CD.configure(state='disabled')
        def checkCallback3():
            print("ring")
            check3.select()
            check2.deselect()
            action_CD = tk.Button(self.scrollFrame.viewPort, text="Configure Directory", command=click_configure_dir, width=25)
            action_CD.grid(column=5, row=8)
        chVarAn = tk.IntVar()
        check2 = tk.Checkbutton(self.scrollFrame.viewPort, text="This machine does NOT require custom directory configuration.", command=checkCallback2, variable=chVarAn)
        check2.deselect()
        check2.grid(column=0, row=8, sticky=tk.W, columnspan=3)
        chVarAm = tk.IntVar()
        check3 = tk.Checkbutton(self.scrollFrame.viewPort, text="This machine does require custom ECU directory configuration.", command=checkCallback3,  variable=chVarAm)
        check3.deselect()
        check3.grid(column=2, row=8, sticky=tk.W, columnspan=3)


        def checkCallback4():
            print("ping")
            check4.select()
            check5.deselect()
            action_CD = tk.Button(self.scrollFrame.viewPort, text="Configure Directory", command=click_configure_dir, width=25)
            action_CD.grid(column=5, row=9)
            action_CD.configure(state='disabled')
        def checkCallback5():
            print("ring")
            check5.select()
            check4.deselect()
            action_CD = tk.Button(self.scrollFrame.viewPort, text="Configure Directory", command=click_configure_dir, width=25)
            action_CD.grid(column=5, row=9)
        chVarBn = tk.IntVar()
        check4 = tk.Checkbutton(self.scrollFrame.viewPort, text="This machine does NOT require custom directory configuration.", command=checkCallback4, variable=chVarBn)
        check4.deselect()
        check4.grid(column=0, row=7, sticky=tk.W, columnspan=3)
        chVarBm = tk.IntVar()
        check5 = tk.Checkbutton(self.scrollFrame.viewPort, text="This machine does require custom ECU directory configuration.", command=checkCallback5,  variable=chVarBm)
        check5.deselect()
        check5.grid(column=2, row=7, sticky=tk.W, columnspan=3)

        def checkCallback6():
            print("ping")
            check6.select()
            check7.deselect()
            action_CD = tk.Button(self.scrollFrame.viewPort, text="Configure Directory", command=click_configure_dir, width=25)
            action_CD.grid(column=5, row=10)
            action_CD.configure(state='disabled')
        def checkCallback7():
            print("ring")
            check7.select()
            check6.deselect()
            action_CD = tk.Button(self.scrollFrame.viewPort, text="Configure Directory", command=click_configure_dir, width=25)
            action_CD.grid(column=5, row=10)
        chVarCn = tk.IntVar()
        check6 = tk.Checkbutton(self.scrollFrame.viewPort, text="This machine does NOT require custom directory configuration.", command=checkCallback6, variable=chVarCn)
        check6.deselect()
        check6.grid(column=0, row=10, sticky=tk.W, columnspan=3)
        chVarCm = tk.IntVar()
        check7 = tk.Checkbutton(self.scrollFrame.viewPort, text="This machine does require custom ECU directory configuration.", command=checkCallback7,  variable=chVarCm)
        check7.deselect()
        check7.grid(column=2, row=10, sticky=tk.W, columnspan=3)

    
    
    def add_remove(self, msg, chosen_programs):
        viable_add = True
        for i in range(len(chosen_programs)):
            if msg[0] == chosen_programs[i][0]:
                chosen_programs.remove(chosen_programs[i])
                viable_add = False
                break
        if (viable_add == True):
            output_file = open("GUI_functions/update.bin", "wb")
            pickle.dump(msg, output_file)
            output_file.close()
            os.system("python3 GUI_functions/select_depend.py")
            input_file = open("GUI_functions/update.bin", "rb")
            new_task = pickle.load(input_file)
            input_file.close()
            chosen_programs.append(new_task)
    
        
    def printMsg_kill(self, msg):
        input_file = open("GUI_functions/Tasks_details.bin", "rb")
        all_programs = pickle.load(input_file)
        input_file.close()

        for i in range(len(all_programs)):
            for j in range(len(msg)):
                if all_programs[i][0] == msg[j][0]:
                    all_programs[i] = msg[j]

        output_file = open("GUI_functions/Tasks_details.bin", "wb")
        pickle.dump(all_programs, output_file)
        output_file.close()
        print(all_programs)
        root.quit()
    

def subsystem_menu():
    input_file = open("GUI_functions/update.bin", "rb")
    this_machine = list(pickle.load(input_file))
    input_file.close()

    # Here the name and IP of the machine displayed as the title of this window.
    input_file.close()

    path = os.path.dirname(os.path.realpath(__file__))

    files = []
    # r=root, d=directories, f = files

    files = [f for f in listdir(path) if isfile(join(path, f))]


    for f in files:
        if ".swp" in f:
            files.remove(f)

    root=tk.Tk()
    root.title(str(this_machine[0])+"@"+this_machine[1])
    menu_frame(root, this_machine).pack(side="top", fill="both", expand=True)
    root.mainloop()
