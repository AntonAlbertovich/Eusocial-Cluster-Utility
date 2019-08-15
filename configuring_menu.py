# This is the main interface menu for the Schedule Builder
# Writen by Anton A Rakos in summer of 2019 for CS 4398, Theory and Practice of Logic Programming at Texas Tech University

import tkinter as tk
import tkinter as ttk
from tkinter import *
from os import walk
import os
import subprocess
from os import listdir
from os.path import isfile, join
import pickle

#These are global variables that may be used throughout the schedule building process.

Schedule = []
Machines = []

Machine_rules=[]
Machine_Netwk=[]
Machine_tools=[]
Machine_hours=[]
Machine_Processor_count=4
Machine_work_hours = []
Machine_time=1


Programs = []

Program_ruels=[]
Program_needs=[]
Program_cost=[]
Program_toolkits=[]

mypath = os.path.dirname(os.path.realpath(__file__))
mypath = mypath+"/Tasks"

possible_programs = [f for f in listdir(mypath) if isfile(join(mypath, f))]
chosen_programs = []
programs = []

Tasks = []

for i in possible_programs:
    if ".py" in i:
        programs.append(i)
    elif ".c" in i:
        programs.append(i)
    elif ".h" in i:
        programs.append(i)
    elif ".asm" in i:
        programs.append(i)
    elif ".f90" in i:
        programs.append(i)
    if ".swp" in i:
        programs.remove(i)
    
for row in range(len(programs)):
    Job = []
    tool_reqs = [] 
    dependencies = [] 
    Job.append(programs[row])
    
    Job.append([0, "N/A"])  #Value 0 indicates that this program is not OS dependent

    Job.append(dependencies)   #Needed Programs
    Job.append(tool_reqs)   #Need tools

    Job.append(1)           #Thread cost

    Tasks.append(Job)

#Original builder for the .bin file which stores detials pertaining to the tasks a cluster may execute.

#print(Tasks)
#output_file= open("GUI_functions/Tasks_details.bin", "wb")
#pickle.dump(Tasks, output_file)
#output_file.close()


class ScrollFrame(tk.Frame):
    # This class allows for a frame which can be scrolled vertically.
    # This is very need as a given cluster may contain many machines or be tasked with many jobs.
    def __init__(self, parent):
        super().__init__(parent) # create a frame (self)

    
        self.canvas = tk.Canvas(self, width = 700, height = 800, borderwidth=0, background="black")         
        self.viewPort = tk.Frame(self.canvas, width = 325, height = 300, background="black")                     
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)  
        self.canvas.configure(yscrollcommand=self.vsb.set)                   

        self.vsb.pack(side="right", fill="y")                                       
        self.canvas.pack(side="left", fill="both", expand=True)                     
        self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",            
                                  tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)                      

    def onFrameConfigure(self, event):                                              
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 


class menu_frame(tk.Frame):
    #This class is the main frame for this part of the menu        
    def __init__(self, root):
        # This initializes the menu
        tk.Frame.__init__(self, root)
        self.scrollFrame = ScrollFrame(self) # add a new scrollable frame.
        mypath = os.path.dirname(os.path.realpath(__file__))
        mypath = mypath+"/Tasks"
        # Tasks is where all the programs which are going to be executed on the various nodes of the cluster.  These are not programs which aid in the fucntionality of the cluster. 
        # Future releases will have another directory called "/Data" which will contain non-executable dependencies which will contain data that needs to exit only on a machine which is running a given program. 
        # As of 3/07/2019 this feature has not been yet built. 
        possible_programs = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        chosen_machines = []
        input_file= open("GUI_functions/Cluster_details.bin", "rb")
        machines = pickle.load(input_file)
        input_file.close()


        for row in range(len(machines)):
            # This loop builds the menu for the configuration of each machine in the cluster.
            a = row
            tk.Checkbutton(self.scrollFrame.viewPort, text= "Configure Machine: " + machines[row][0], relief="solid",command=lambda x=a:self.add_remove(machines[x], chosen_machines), width=30).grid(row=row + 7, column=0)
        

        tk.Label(self.scrollFrame.viewPort, text="Program Dependency Options", width=40).grid(row= 0, column=0)
        # Program Dependency Options is the section of the menu which allows for each program's needs to be enetered into the data structure which will later build the ASP file for the schedule. 
        #Programs are organized by file type, at this time ECU supports the organization of Python, Fortran, C, C++, and Assembly files.
        

        tk.Label(self.scrollFrame.viewPort, text="Reset Options").grid(row= 0, column=2)
        # Reset options is the section of the menu which allows for the data structures pertaining to machines and tasks to be cleared.
        tk.Label(self.scrollFrame.viewPort, text="Machine Options", width=40).grid(row=6, column=0)
        # Machine options is the section of the menu which allows for the individual configuration of each machine in the cluster, this section is built with the loop above.

        tk.Label(self.scrollFrame.viewPort, text="Number of Theads Needed for processing", width=40).grid(row=8+len(machines), column=0)

        tk.Button(self.scrollFrame.viewPort, text="Python program dependency settings", command=lambda x=a: self.py_settings(".py"), width=35, relief="solid").grid(row= 1, column=0)

        tk.Button(self.scrollFrame.viewPort, text="Fortran program dependency settings", command=lambda x=a: self.fr_settings(".f90"), width=35, relief="solid").grid(row= 2, column=0)
        tk.Button(self.scrollFrame.viewPort, text="C program dependency settings", command=lambda x=a: self.c_settings(".c"), width=35, relief="solid").grid(row= 3, column=0)
        tk.Button(self.scrollFrame.viewPort, text="C++ program dependency settings", command=lambda x=a: self.cpp_settings(".cpp"), width=35, relief="solid").grid(row= 4, column=0)
        tk.Button(self.scrollFrame.viewPort, text="Assembly program dependency settings", command=lambda x=a: self.asm_settings(".asm"), width=35, relief="solid").grid(row= 5, column=0)


        
        chosen_programs = []
        programs = []
        thread_cost = []
        j = 0 

        tk.Button(self.scrollFrame.viewPort, text="Reset All Machines", command=lambda x=a: self.reset_machines("reset"), width=15, relief="solid").grid(row= 1, column=2)
        tk.Button(self.scrollFrame.viewPort, text="Reset All Programs", command=lambda x=a: self.reset_programs(list(machines), thread_cost), width=15, relief="solid").grid(row= 2, column=2)
        tk.Label(self.scrollFrame.viewPort, text="View Options").grid(row= 3, column=2)
        tk.Button(self.scrollFrame.viewPort, text="View All Machines", command=lambda x=a: self.view_machines("reset"), width=15, relief="solid").grid(row= 4, column=2)
        tk.Button(self.scrollFrame.viewPort, text="View All Programs", command=lambda x=a: self.view_programs(list(machines), thread_cost), width=15, relief="solid").grid(row= 5, column=2)

        self.scrollFrame.pack(side="top", fill="both", expand=True)

        # These loops help organized the programs for the /Tasks directory, they are organized by file type. 
        for i in possible_programs:
            if ".py" in i:
                programs.append(i)
                thread_cost.append([i,str(1)])
            
        for i in possible_programs:
            if ".c" in i:
                programs.append(i)
                thread_cost.append([i,str(1)])
            if ".cpp" in i:
                programs.remove(i)
                thread_cost.remove([i,str(1)])

        for i in possible_programs:
            if ".cpp" in i:
                programs.append(i)
                thread_cost.append([i,str(1)])


        for i in possible_programs:
            if ".f90" in i:
                programs.append(i)
                thread_cost.append([i,str(1)])
        
        for i in possible_programs:
            if ".asm" in i:
                programs.append(i)
                thread_cost.append([i,str(1)])

        for row in range(len(programs)):
            a = row
            tk.Button(self.scrollFrame.viewPort, text=programs[row], width=25, relief="solid").grid(row=a+9+len(machines), column=0)
            tk.Button(self.scrollFrame.viewPort, text="Increase Cost", command=lambda x=a: self.click_change_up(thread_cost, x, machines)).grid(row=a+9+len(machines), column=1)
            tk.Button(self.scrollFrame.viewPort, text="Thread Cost: " + thread_cost[a][1]).grid(row=a+9+len(machines), column=2)
            j = j + 1
        
        
        tk.Button(self.scrollFrame.viewPort, text="Update Program Thread Costs", command=lambda x=a: self.update_cost(thread_cost), width=25).grid(row=row+10+len(machines), column=0)
        # This button must be pused inorder to commit the updated thread costs displayed in the interface.
        # A current issue is that the tasks displayed may not currently reflect the thread costs in the task_details data structure.

        tk.Label(self.scrollFrame.viewPort, text="Schedule Options", width=31 ).grid(row= row+11+len(machines), column=0)
        tk.Button(self.scrollFrame.viewPort, text="Build Schedule [15s Attempt]", width=28, command=lambda x=a: self.build_schedule_15(machines)).grid(row=row+12+len(machines), column=0)
        tk.Button(self.scrollFrame.viewPort, text="Build Schedule [60s Attempt]", width=28, command=lambda x=a: self.build_schedule_30(machines)).grid(row=row+13+len(machines), column=0)
        tk.Button(self.scrollFrame.viewPort, text="Build Schedule [5m Attempt]", width=28, command=lambda x=a: self.build_schedule_300(machines)).grid(row=row+14+len(machines), column=0)
        tk.Label(self.scrollFrame.viewPort, text="Schedule Build Not Yet Attempted", width=31).grid(row= row+15+len(machines), column=0)
        tk.Button(self.scrollFrame.viewPort, text="View Schedule", width=28, command=lambda x=a: self.view_schedule(chosen_programs),state = 'disabled').grid(row=row+16+len(machines), column=0)
        tk.Button(self.scrollFrame.viewPort, text="Exit Schedule Builder", width=28, command=lambda x=a: self.printMsg_kill(chosen_programs)).grid(row=row+17+len(machines), column=0)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
    def add_remove(self, selected, chosen):
        # If a machine's details are configured this function allows for those changes to be committed to the appropriate data structure. 
        viable_add = True
        for i in range(len(chosen)):
            if selected == chosen[i]:
                chosen.remove(selected)
                viable_add = False
                break
        if (viable_add == True):
            output_file = open("GUI_functions/update.bin", "wb")
            # Here update.bin contains the information which specifies which machine is to edited by machine_submenu.py
            machine_data = []
            machine_data.append(selected[0])
            machine_data.append(selected[1])
            pickle.dump(machine_data, output_file)
            output_file.close()
            # machine_submenu.py is a script which edits the data structure pertaining to the machines in the cluster

            from GUI_functions.sub_system_menu import subsystem_menu
            subsystem_menu()
            #os.system("python3 GUI_functions/machine_submenu.py")
            chosen.append(selected)
            print(chosen)
    
    
    def py_settings(self, msg):
        # This function opens the script pertaining to python dependencies. 
        os.system("python3 GUI_functions/select_py_GUI.py")
    def fr_settings(self, msg):
        # This function opens the script pertaining to fortran dependencies. 
        os.system("python3 GUI_functions/select_f90_GUI.py")
    def cpp_settings(self, msg):
        os.system("python3 GUI_functions/select_cpp_GUI.py")
        # This function opens the script pertaining to C++ dependencies. 
    def c_settings(self, msg):
        os.system("python3 GUI_functions/select_c_GUI.py")
        # This function opens the script pertaining to C dependencies. 
    def asm_settings(self, msg):
        os.system("python3 GUI_functions/select_asm_GUI.py")
        # This function opens the script pertaining to assembly dependencies. 
    
    def click_change_up(self, costs, a, machines):
        #This increments the thread cost of a particular task.
        cost_value = int(costs[a][1])
        cost_value = cost_value + 1
        costs[a][1] = str(cost_value) 
        tk.Button(self.scrollFrame.viewPort, text="Thread Cost: " + costs[a][1]).grid(row=a+9+len(machines), column=2)
        tk.Button(self.scrollFrame.viewPort, text="Decrease Cost", command=lambda x=a: self.click_change_down(costs, x, machines)).grid(row=a+9+len(machines), column=3)
    
    def click_change_down(self, costs, a, machines):
        #This decrements the thread cost of a particular task.
        cost_value = int(costs[a][1])
        if(cost_value > 1):
            cost_value = cost_value - 1
            costs[a][1] = str(cost_value) 
            tk.Button(self.scrollFrame.viewPort, text="Thread Cost: " + costs[a][1]).grid(row=a+9+len(machines), column=2)
        else:
            tk.Button(self.scrollFrame.viewPort, text="Decrease Cost", state='disabled').grid(row=a+9+len(machines), column=3)
    
    def update_cost(self, msg):
        # This will update the data structure pertaining to the thread cost of each task to the displayed costs for said task in the interface. 
        input_file = open("GUI_functions/Tasks_details.bin", "rb")
        all_tasks= list(pickle.load(input_file))
        input_file.close()
        for i in range(len(msg)):
            for j in range(len(all_tasks)):
                if msg[i][0] == all_tasks[j][0]:
                    all_tasks[j][4] = msg[i][1]
                    break
        output_file = open("GUI_functions/Tasks_details.bin", "wb")
        pickle.dump(all_tasks, output_file)
        output_file.close()




    def printMsg_kill(self, msg):
        # This exits the window.
        
        root.quit()
        
    def reset_machines(self, msg):
        # This will reset all the machines in the cluster to default settings, these include a core count of 4 and an OS of Ubuntu 18.04 [Desktop Edition].
        # Default assumes that no toolkits are installed on any machines.
        # Default assumes that no machine is networked to any other machine.
        input_file= open("GUI_functions/Cluster_details.bin", "rb")
        all_tasks= list(pickle.load(input_file))
        input_file.close()
        for i in range(len(all_tasks)):
            all_tasks[i][2] = []
            all_tasks[i][3] = []
            all_tasks[i][4] = []
            all_tasks[i][5] = ["python3 ", "gfortran ", "gcc ", "g++", "nasm -felf64 "]
            all_tasks[i][6] = 4
            all_tasks[i][7] = "Ubuntu 18.04 [Desktop Edition]"
        
        output_file = open("GUI_functions/Cluster_details.bin", "wb")
        # This updates the data structure pertaining to the machines in the cluster.
        # This will not completely reset the cluster, if there were initially n many machines prior to a reset then n many machines will remain after the reset, names and IPs will not be changeds. 
        pickle.dump(all_tasks, output_file)
        output_file.close()

    def reset_programs(self, machines, costs):
        # This wil reset all the tasks in the cluster to default settings.
        # Default assumes that a task is not dependent on an OS.
        # Default assumes that multi-threading is not used by any task, thus that the tasks do not require more than one core.
        input_file= open("GUI_functions/Tasks_details.bin", "rb")
        all_tasks= list(pickle.load(input_file))
        input_file.close() 
        for i in range(len(all_tasks)):
            print(all_tasks[i])
            all_tasks[i][1] = [0, "N/A"] # No OS specified
            all_tasks[i][2] = []
            all_tasks[i][3] = []
            all_tasks[i][4] = 1
            costs[i][1] = str(0) 
            tk.Button(self.scrollFrame.viewPort, text="Thread Cost: " + str(all_tasks[i][4])).grid(row=i+9+len(machines), column=2)
            tk.Button(self.scrollFrame.viewPort, text="Decrease Cost", state='disabled').grid(row=i+9+len(machines), column=3)

    def view_machines(self, msg):
        # This function simply runs a script which will show the contents of the Cluster_details data structure in a GUI.
        os.system("python3 GUI_functions/print_machines.py")
        
    def view_programs(self, machines, costs):
        # This function simply runs a script which will show the contents of the Tasks_details data structure in a GUI.
        os.system("python3 GUI_functions/print_programs.py")

    def build_schedule_15(self, machines):
        # This function first runs the script which will build the ASP script, and then attempts to build the script with a 15 secound time limit. 
        # If the ASP is not solved within the limited time then the program prints a lable to the GUI inidcating that the failure.
        # If the ASP is solved then a success message is printed to the GUI and a button which allows for the ASP output to be viewed is enabled.
        # This function will parse the output of asp.lp if the solver is successful.
        os.system("python3 GUI_functions/build_asp.py")
        output = str(subprocess.check_output("clingo --time-limit=15 GUI_functions/asp.lp", shell=True))
        out = output.split("\\n")
        solution = []
        satisfiable = False
        for i in range(len(out)):
                if out[i] == "SATISFIABLE":
                    satisfiable = True
                    solution = out[i-1].split(" ")
                    break
        if satisfiable == True:
            tk.Label(self.scrollFrame.viewPort, text="15s Schedule Build Successful", width=31).grid(row= row+15+len(machines), column=0)
            tk.Button(self.scrollFrame.viewPort, text="View Schedule", width=28, command=lambda x=0: self.view_schedule(solution)).grid(row=row+16+len(machines), column=0)
        else:
            tk.Label(self.scrollFrame.viewPort, text="15s Schedule Build Failed", width=31).grid(row= row+15+len(machines), column=0)
            tk.Button(self.scrollFrame.viewPort, text="View Schedule", width=28, command=lambda x=0: self.view_schedule(solution), state = 'disabled').grid(row=row+16+len(machines), column=0)

    def build_schedule_60(self, machines):
        # This function first runs the script which will build the ASP script, and then attempts to build the script with a 60 secound time limit. 
        # If the ASP is not solved within the limited time then the program prints a lable to the GUI inidcating that the failure.
        # If the ASP is solved then a success message is printed to the GUI and a button which allows for the ASP output to be viewed is enabled.
        # This function will parse the output of asp.lp if the solver is successful.
        os.system("python3 GUI_functions/build_asp.py")
        output = str(subprocess.check_output("clingo --time-limit=60 GUI_functions/asp.lp", shell=True))
        out = output.split("\\n")
        solution = []
        satisfiable = False
        for i in range(len(out)):
                if out[i] == "SATISFIABLE":
                    satisfiable = True
                    solution = out[i-1].split(" ")
                    break
        if satisfiable == True:
            tk.Label(self.scrollFrame.viewPort, text="60s Schedule Build Successful", width=31).grid(row= row+15+len(machines), column=0)
            tk.Button(self.scrollFrame.viewPort, text="View Schedule", width=28, command=lambda x=0: self.view_schedule(solution)).grid(row=row+16+len(machines), column=0)
        else:
            tk.Label(self.scrollFrame.viewPort, text="60s Schedule Build Failed", width=31).grid(row= row+15+len(machines), column=0)
            tk.Button(self.scrollFrame.viewPort, text="View Schedule", width=28, command=lambda x=0: self.view_schedule(solution), state = 'disabled').grid(row=row+16+len(machines), column=0)
    
    def build_schedule_300(self, machines):
        # This function first runs the script which will build the ASP script, and then attempts to build the script with a 300 secound time limit. 
        # If the ASP is not solved within the limited time then the program prints a lable to the GUI inidcating that the failure.
        # If the ASP is solved then a success message is printed to the GUI and a button which allows for the ASP output to be viewed is enabled.
        # This function will parse the output of asp.lp if the solver is successful.
        os.system("python3 GUI_functions/build_asp.py")
        output = str(subprocess.check_output("clingo --time-limit=300 GUI_functions/asp.lp", shell=True))
        out = output.split("\\n")
        solution = []
        satisfiable = False
        for i in range(len(out)):
                if out[i] == "SATISFIABLE":
                    satisfiable = True
                    solution = out[i-1].split(" ")
                    break
        if satisfiable == True:
            tk.Label(self.scrollFrame.viewPort, text="5m Schedule Build Successful", width=31).grid(row= row+15+len(machines), column=0)
            tk.Button(self.scrollFrame.viewPort, text="View Schedule", width=28, command=lambda x=0: self.view_schedule(solution)).grid(row=row+16+len(machines), column=0)
        else:
            tk.Label(self.scrollFrame.viewPort, text="5m Schedule Build Failed", width=31).grid(row= row+15+len(machines), column=0)
            tk.Button(self.scrollFrame.viewPort, text="View Schedule", width=28, command=lambda x=0: self.view_schedule(solution), state = 'disabled').grid(row=row+16+len(machines), column=0)
    
    def view_schedule(self, solution):
        # This function will call the view_asp.py script, a program which displays a task schedule in a GUI.
        output_file = open("GUI_functions/update.bin", "wb")
        final = 0
        for i in range(len(solution)):
            this_turn = solution[i].split(",")
            this_turn[2] = this_turn[2].replace(")", "")
            this_final = int(this_turn[2])
            if this_final > final:
                final = this_final

        machine_data = []
        machine_data.append(0)
        machine_data.append(solution)
        pickle.dump(machine_data, output_file)
        output_file.close()
        while(True):
            os.system("python3 GUI_functions/view_asp.py")
            
            input_file = open("GUI_functions/update.bin", "rb")
            all_turns = list(pickle.load(input_file))
            input_file.close()
            turn = int(all_turns[0])
            if turn >= final:
                break
            


def configuring_build():
    # The main for the schedule builder GUI.
    root=tk.Tk()
    root.title('Schedule Builder')
    menu_frame(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
