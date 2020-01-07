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

    
        self.canvas = tk.Canvas(self, width = 1200, height = 500, borderwidth=0)
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
    


        def click_set_c():
            # This allows the user to enter a default execution command for all C scripts.
            tk.Label(self.scrollFrame.viewPort, width = 45, text='Pre-execution abort command:~$ ' + c_nameEntered.get()).grid(column=2, row=6)
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
            tk.Label(self.scrollFrame.viewPort, text='ASM Executed with: $' + asm_nameEntered.get()).grid(column=2, row=14)
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
            tk.Label(self.scrollFrame.viewPort, width = 45, text='Pre-execution Command:~$ ' + f90_nameEntered.get()).grid(column=2, row=2)
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
            tk.Label(self.scrollFrame.viewPort, width = 45, text='Program Executed with:~$ ' + cpp_nameEntered.get()).grid(column=2, row=8)
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

        def click_configure_networks():
                # This function opens the window for selecting what machines this machine may acccess.
                print("Setting up Network...")
                from GUI_functions.select_networks import networks_GUI
                networks_GUI()
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
                # This function opens the window for selecting which toolkits are on this machine.
                print("Setting up toolkits...")
                from GUI_functions.select_toolkits import tool_GUI
                tool_GUI()
                input_file = open("GUI_functions/update.bin", "rb")
                this_update = list(pickle.load(input_file))
                input_file.close()

                input_file= open("GUI_functions/Cluster_details.bin", "rb")
                machines = pickle.load(input_file)
                input_file.close()

                for i in range(len(machines)):
                    print("ping toolkit")
                    if this_machine[1] == machines[i][1]:
                        machines[i][3] = this_update
                        output_file= open("GUI_functions/Cluster_details.bin", "wb")
                        pickle.dump(machines, output_file)
                        output_file.close()
                        print(machines)
                        break


        def click_configure_avil():
                # This function opens the window for selecting what times a machine is available at.
                # As of 7/05/2019 this feature has not been fully integrated yet.
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
                    print("ping avil")
                    if this_machine[1] == machines[i][1]:
                        machines[i][4] = this_update
                        output_file= open("GUI_functions/Cluster_details.bin", "wb")
                        pickle.dump(machines, output_file)
                        output_file.close()
                        print(machines)
                        break

        def click_configure_dir():
                # This function opens the window for entering a custom directory for a machine in a given cluster.
                # As of 8/15/2019 this feature has not been fully integrated yet.
                print("Setting up directory path...")

        def click_configure_time():
                # This function opens the window for entering the time zone of a machine in a cluster if said machine is not configured to UTC.
                # As of 8/15/2019 this feature has not been fully integrated yet.
                print("Setting up time zone...")

        tk.Frame.__init__(self, root)
        self.scrollFrame = ScrollFrame(self) # add a new scrollable frame.


        self.scrollFrame.pack(side="top", fill="both", expand=True)
    


        tk.Label(self.scrollFrame.viewPort, text="Leave blank if no pre-execution command is needed.").grid(column=2, row=2)
        #tk.Label(self.scrollFrame.viewPort, text="C++").grid(column=2, row=4)
        tk.Label(self.scrollFrame.viewPort, text="Leave blank if none is needed.").grid(column=2, row=5)
        tk.Label(self.scrollFrame.viewPort, text="Leave blank if none is needed.").grid(column=2, row=6)


        f90_name = tk.StringVar()
        f90_nameEntered = tk.Entry(self.scrollFrame.viewPort, width=25, textvariable=f90_name)
        f90_nameEntered.grid(column=1, row=2)





        asm_name = tk.StringVar()
        asm_nameEntered = tk.Entry(self.scrollFrame.viewPort, width=25, textvariable=asm_name)
        asm_nameEntered.grid(column=1, row=14)

        #cc_name = tk.StringVar()
        #cc_nameEntered = tk.Entry(self.scrollFrame.viewPort, width=5, textvariable=cc_name)
        #cc_nameEntered.grid(column=1, row=6)

        click_set_f90 = tk.Button(self.scrollFrame.viewPort, text="Set Pre-Execution Command", command=click_set_f90, width=35 )
        click_set_f90.grid(column=0, row=2)



        click_set_c = tk.Button(self.scrollFrame.viewPort, text="Set Abort Phrase", command=click_set_c, width=35)
        click_set_c.grid(column=0, row=6)

        click_set_cpp = tk.Button(self.scrollFrame.viewPort, text="Program Execution Command", command=click_set_cpp, width=35)
        click_set_cpp.grid(column=0, row=8)

        cpp_name = tk.StringVar()
        cpp_nameEntered = tk.Entry(self.scrollFrame.viewPort, width=25, textvariable=cpp_name)
        cpp_nameEntered.grid(column=1, row=8)

        click_set_asm = tk.Button(self.scrollFrame.viewPort, text="Set Abort Command", command=click_set_asm, width=35)
        click_set_asm.grid(column=0, row=14)

        #click_set_cc = tk.Button(self.scrollFrame.viewPort, text="Set Custom Core Count", command=click_set_cc, width=35)
        #click_set_cc.grid(column=0, row=6)

        tk.Label(self.scrollFrame.viewPort, text="Set a command to run before attempting program execution").grid(column=0, row=0)
        tk.Label(self.scrollFrame.viewPort, text="Set the command which will run this program").grid(column=0, row=7)
        def checkCallback0():
            print("ping 0")
            check0.select()
            check1.deselect()
        def checkCallback1():
            print("ring 1")
            check1.select()
            check0.deselect()
        chVarDn = tk.IntVar()
        check0 = tk.Checkbutton(self.scrollFrame.viewPort, text=this_machine[0] + " requires a pre-execution command.", command=checkCallback0, variable=chVarDn)
        check0.deselect()
        check0.grid(column=0, row=1, sticky=tk.W, columnspan=3)
        chVarDm = tk.IntVar()
        check1 = tk.Checkbutton(self.scrollFrame.viewPort, text=this_machine[0] + " is executed with a single command.", command=checkCallback1,  variable=chVarDm)
        check1.deselect()
        check1.grid(column=2, row=1, sticky=tk.W, columnspan=3)


        c_name = tk.StringVar()
        c_nameEntered = tk.Entry(self.scrollFrame.viewPort, width=25, textvariable=c_name)
        c_nameEntered.grid(column=1, row=6)

        tk.Label(self.scrollFrame.viewPort, text="If Pre-Executions fails:").grid(column=0, row=3)
        def checkCallback2():
            print("ping 2")
            check2.select()
            check3.deselect()
        def checkCallback3():
            print("ring 3")
            check3.select()
            check2.deselect()
        chVarAn = tk.IntVar()
        check2 = tk.Checkbutton(self.scrollFrame.viewPort, text= "Try again on a different machine.", command=checkCallback2, variable=chVarAn)
        check2.deselect()
        check2.grid(column=0, row=4, sticky=tk.W, columnspan=3)
        chVarAm = tk.IntVar()
        check3 = tk.Checkbutton(self.scrollFrame.viewPort, text= "Ignore program pre-execution's exit code.", command=checkCallback3,  variable=chVarAm)
        check3.deselect()
        check3.grid(column=2, row=4, sticky=tk.W, columnspan=3)


        def checkCallback4():
            print("ping 4")
            check4.select()
            check5.deselect()
        def checkCallback5():
            print("ring 5")
            check5.select()
            check4.deselect()
        chVar4 = tk.IntVar()
        check4 = tk.Checkbutton(self.scrollFrame.viewPort, text="Set an abort command.", command=checkCallback4, variable=chVar4)
        check4.deselect()
        check4.grid(column=0, row=5, sticky=tk.W, columnspan=3)
        chVar5 = tk.IntVar()
        check5 = tk.Checkbutton(self.scrollFrame.viewPort, text="Do not set a pre-execution abort phrase.", command=checkCallback5,  variable=chVar5)
        check5.deselect()
        check5.grid(column=2, row=5, sticky=tk.W, columnspan=3)

        def checkCallback6():
            print("ping 6")
            check6.select()
            check7.deselect()
        def checkCallback7():
            print("ring 7")
            check7.select()
            check6.deselect()
        
        tk.Label(self.scrollFrame.viewPort, text="If Executions fails:").grid(column=0, row=11)
        chVarCn = tk.IntVar()
        check6 = tk.Checkbutton(self.scrollFrame.viewPort, text="Try again on a different machine.", command=checkCallback6, variable=chVarCn)
        check6.deselect()
        check6.grid(column=0, row=12, sticky=tk.W, columnspan=3)
        chVarCm = tk.IntVar()
        check7 = tk.Checkbutton(self.scrollFrame.viewPort, text="Ignore program execution's exit code.", command=checkCallback7,  variable=chVarCm)
        check7.deselect()
        check7.grid(column=2, row=12, sticky=tk.W, columnspan=3)



        def checkCallback8():
            print("ping 8")
            check8.select()
            check9.deselect()
        def checkCallback9():
            print("ring")
            check9.select()
            check8.deselect()
        chVar8 = tk.IntVar()
        check8 = tk.Checkbutton(self.scrollFrame.viewPort, text="Terminate all opertations if this program can not be completed.", command=checkCallback8, variable=chVar8)
        check8.deselect()
        check8.grid(column=0, row=13, sticky=tk.W, columnspan=3)
        chVar9 = tk.IntVar()
        check9 = tk.Checkbutton(self.scrollFrame.viewPort, text="Only terminate operation dependent on this program.", command=checkCallback9,  variable=chVar9)
        check9.deselect()
        check9.grid(column=2, row=13, sticky=tk.W, columnspan=3)
        
        
        tk.Label(self.scrollFrame.viewPort, text="Set Execution Time Constraint").grid(column=0, row=15)
        tk.Label(self.scrollFrame.viewPort, text="Set Timer Condition ").grid(column=2, row=15)

        archit= ['Not Aplicable', 'Time Pre-Execution Phase', 'Time Execution Phase', 'Time Both Phases Individually', 'Time Both Phases Together']
        os_distro= ['No Time Constraint', '15 Seconds', '60 Seconds', '5 Minutes', '60 Minutes', '24 Hours', '72 Hours']

        def os_deselect(keep):
            if keep != 0:
                OS_0.deselect()
            if keep != 1:
                OS_1.deselect()
            if keep != 2:
                OS_2.deselect()
            if keep != 3:
                OS_3.deselect()
            if keep != 4:
                OS_4.deselect()
            if keep != 5:
                OS_5.deselect()

        def ar_deselect(keep):
            if keep != 0:
                AR_0.deselect()
            if keep != 1:
                AR_1.deselect()
            if keep != 2:
                AR_2.deselect()
            if keep != 3:
                AR_3.deselect()
            if keep != 4:
                AR_4.deselect()

        def os_Call_0():
            print(os_distro[0])
            os_deselect(0)

        def os_Call_1():
            print(os_distro[1])
            os_deselect(1)

        def os_Call_2():
            print(os_distro[2])
            os_deselect(2)

        def os_Call_3():
            print(os_distro[3])
            os_deselect(3)

        def os_Call_4():
            print(os_distro[4])
            os_deselect(4)

        def os_Call_5():
            print(os_distro[5])
            os_deselect(5)

        def os_Call_6():
            print(os_distro[6])
            os_deselect(6)

        def ar_Call_0():
            print(archit[0])
            ar_deselect(0)

        def ar_Call_1():
            print(archit[1])
            ar_deselect(1)

        def ar_Call_2():
            print(archit[2])
            ar_deselect(2)

        def ar_Call_3():
            print(archit[3])
            ar_deselect(3)

        def ar_Call_4():
            print(archit[4])
            ar_deselect(4)

        chOS_0 = tk.IntVar()
        OS_0 = tk.Checkbutton(self.scrollFrame.viewPort, text=os_distro[0], command=os_Call_0, variable=chOS_0)
        OS_0.deselect()
        OS_0.grid(column=0, row=16, sticky=tk.W, columnspan=3)
        
        chOS_1 = tk.IntVar()
        OS_1 = tk.Checkbutton(self.scrollFrame.viewPort, text=os_distro[1], command=os_Call_1, variable=chOS_1)
        OS_1.deselect()
        OS_1.grid(column=0, row=17, sticky=tk.W, columnspan=3)

        chOS_2 = tk.IntVar()
        OS_2 = tk.Checkbutton(self.scrollFrame.viewPort, text=os_distro[2], command=os_Call_2, variable=chOS_2)
        OS_2.deselect()
        OS_2.grid(column=0, row=18, sticky=tk.W, columnspan=3)
        
        chOS_3 = tk.IntVar()
        OS_3 = tk.Checkbutton(self.scrollFrame.viewPort, text=os_distro[3], command=os_Call_3, variable=chOS_3)
        OS_3.deselect()
        OS_3.grid(column=0, row=19, sticky=tk.W, columnspan=3)

        chOS_4 = tk.IntVar()
        OS_4 = tk.Checkbutton(self.scrollFrame.viewPort, text=os_distro[4], command=os_Call_4, variable=chOS_4)
        OS_4.deselect()
        OS_4.grid(column=0, row=20, sticky=tk.W, columnspan=3)

        chOS_5 = tk.IntVar()
        OS_5 = tk.Checkbutton(self.scrollFrame.viewPort, text=os_distro[5], command=os_Call_4, variable=chOS_4)
        OS_5.deselect()
        OS_5.grid(column=0, row=21, sticky=tk.W, columnspan=3)

        chOS_6 = tk.IntVar()
        OS_6 = tk.Checkbutton(self.scrollFrame.viewPort, text=os_distro[6], command=os_Call_4, variable=chOS_4)
        OS_6.deselect()
        OS_6.grid(column=0, row=21, sticky=tk.W, columnspan=3)

        chAR_0 = tk.IntVar()
        AR_0 = tk.Checkbutton(self.scrollFrame.viewPort, text=archit[0], command=ar_Call_0, variable=chAR_0)
        AR_0.deselect()
        AR_0.grid(column=2, row=16, sticky=tk.W, columnspan=3)
        
        chAR_1 = tk.IntVar()
        AR_1 = tk.Checkbutton(self.scrollFrame.viewPort, text=archit[1], command=ar_Call_1, variable=chAR_1)
        AR_1.deselect()
        AR_1.grid(column=2, row=17, sticky=tk.W, columnspan=3)

        chAR_2 = tk.IntVar()
        AR_2 = tk.Checkbutton(self.scrollFrame.viewPort, text=archit[2], command=ar_Call_2, variable=chAR_2)
        AR_2.deselect()
        AR_2.grid(column=2, row=18, sticky=tk.W, columnspan=3)
        
        chAR_3 = tk.IntVar()
        AR_3 = tk.Checkbutton(self.scrollFrame.viewPort, text=archit[3], command=ar_Call_3, variable=chAR_3)
        AR_3.deselect()
        AR_3.grid(column=2, row=19, sticky=tk.W, columnspan=3)

        chAR_4 = tk.IntVar()
        AR_4 = tk.Checkbutton(self.scrollFrame.viewPort, text=archit[4], command=ar_Call_4, variable=chAR_4)
        AR_4.deselect()
        AR_4.grid(column=2, row=20, sticky=tk.W, columnspan=3)
        
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
        def exe_dir():
            from GUI_functions.exe_directory_options import Exe_directory_options
            Exe_directory_options()


        action_Q = tk.Button(self.scrollFrame.viewPort, text="Build Execution Directory", command=exe_dir, width=25)
        action_Q.grid(column=0, row=24)
        action_Q = tk.Button(self.scrollFrame.viewPort, text="Save Cahnges", command=printMsg_kill, width=25)
        action_Q.grid(column=0, row=25)


def exe_menu():
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
    root.title(str(this_machine[0]))
    menu_frame(root, this_machine).pack(side="top", fill="both", expand=True)
    root.mainloop()
