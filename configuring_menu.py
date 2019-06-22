import tkinter as tk
import tkinter as ttk
from tkinter import *
from os import walk
import os
from os import listdir
from os.path import isfile, join
import pickle

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

print(Tasks)
output_file= open("GUI_functions/Tasks_details.bin", "wb")
pickle.dump(Tasks, output_file)
output_file.close()


class ScrollFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent) # create a frame (self)

    
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")          #place canvas on self
        self.viewPort = tk.Frame(self.canvas, background="#ffffff")                    #place a frame on the canvas, this frame will hold the child widgets 
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview) #place a scrollbar on self 
        self.canvas.configure(yscrollcommand=self.vsb.set)                          #attach scrollbar action to scroll of canvas

        self.vsb.pack(side="right", fill="y")                                       #pack scrollbar to right of self
        self.canvas.pack(side="left", fill="both", expand=True)                     #pack canvas to left of self and expand to fil
        self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",            #add view port frame to canvas
                                  tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.

    def onFrameConfigure(self, event):                                              
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.


class Example(tk.Frame):
    
    def __init__(self, root):

        tk.Frame.__init__(self, root)
        self.scrollFrame = ScrollFrame(self) # add a new scrollable frame.
        mypath = os.path.dirname(os.path.realpath(__file__))
        mypath = mypath+"/GUI_functions/Tasks"
        possible_programs = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        chosen_machines = []
        input_file= open("GUI_functions/Cluster_details.bin", "rb")
        machines = pickle.load(input_file)
        input_file.close()

        #machines = [["Machine 1", "192.168.1.00" ], ["Machine 2", "192.168.1.01" ], ["Machine 3", "192.168.1.02" ],["Machine 4", "192.168.1.03" ]]

        for row in range(len(machines)):
            a = row
            tk.Checkbutton(self.scrollFrame.viewPort, text= "Configure Machine: " + machines[row][0], relief="solid",command=lambda x=a:self.add_remove(machines[x], chosen_machines), width=30).grid(row=row + 7, column=0)
                    
        tk.Label(self.scrollFrame.viewPort, text="Program Dependency Options", width=40).grid(row= 0, column=0)
        tk.Label(self.scrollFrame.viewPort, text="Program Thead Options", width=40).grid(row=6, column=0)
        tk.Label(self.scrollFrame.viewPort, text="Number of Theads Needed for processing", width=40).grid(row=8+len(machines), column=0)

        tk.Button(self.scrollFrame.viewPort, text="Python program dependency settings", command=lambda x=a: self.py_settings(".py"), width=35, relief="solid").grid(row= 1, column=0)
        tk.Button(self.scrollFrame.viewPort, text="Fortran program dependency settings", command=lambda x=a: self.fr_settings(".f90"), width=35, relief="solid").grid(row= 2, column=0)
        tk.Button(self.scrollFrame.viewPort, text="C program dependency settings", command=lambda x=a: self.c_settings(".c"), width=35, relief="solid").grid(row= 3, column=0)
        tk.Button(self.scrollFrame.viewPort, text="C++ program dependency settings", command=lambda x=a: self.cpp_settings(".cpp"), width=35, relief="solid").grid(row= 4, column=0)
        tk.Button(self.scrollFrame.viewPort, text="Assembly program dependency settings", command=lambda x=a: self.asm_settings(".asm"), width=35, relief="solid").grid(row= 5, column=0)

        
        
        
        tk.Button(self.scrollFrame.viewPort, text="Save changes to all marked items", command=lambda x=a: self.printMsg_kill(chosen_programs), width=30).grid(row= len(machines) + 7, column=0)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
        
        chosen_programs = []
        programs = []
        thread_cost = []
        j = 0 
        for i in possible_programs:
            print("---------------------")
            print(i)
            if ".py" in i:
                programs.append(i)
                thread_cost.append([i,str(1)])
            elif ".c" in i:
                programs.append(i)
                thread_cost.append([i,str(1)])
            elif ".f90" in i:
                programs.append(i)
                thread_cost.append([i,str(1)])
            elif ".asm" in i:
                programs.append(i)
                thread_cost.append([i,str(1)])

        for row in range(len(programs)):
            a = row
            tk.Button(self.scrollFrame.viewPort, text=programs[row], width=25, relief="solid").grid(row=a+9+len(machines), column=0)
            tk.Button(self.scrollFrame.viewPort, text="Increase Cost", command=lambda x=a: self.click_change_up(thread_cost, x, machines)).grid(row=a+9+len(machines), column=1)
            tk.Button(self.scrollFrame.viewPort, text="Thread Cost: " + thread_cost[a][1]).grid(row=a+9+len(machines), column=2)
            j = j + 1
        
        
        tk.Button(self.scrollFrame.viewPort, text="Update Program Thread Costs", command=lambda x=a: self.update_cost(thread_cost), width=25).grid(row=row+10+len(machines), column=0)
        tk.Button(self.scrollFrame.viewPort, text="Done, Build Schedule", command=lambda x=a: self.printMsg_kill(chosen_programs)).grid(row=row+11+len(machines), column=0)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
    def add_remove(self, selected, chosen):
        viable_add = True
        for i in range(len(chosen)):
            if selected == chosen[i]:
                chosen.remove(selected)
                viable_add = False
                break
        if (viable_add == True):

            output_file = open("GUI_functions/update.bin", "wb")
            machine_data = []
            machine_data.append(selected[0])
            machine_data.append(selected[1])
            print("? " + str(machine_data))
            pickle.dump(machine_data, output_file)
            output_file.close()
            os.system("python3 GUI_functions/machine_submenu.py")
            chosen.append(selected)
    def py_settings(self, msg):
        print(msg)
        os.system("python3 GUI_functions/select_py_GUI.py")
    def fr_settings(self, msg):
        print(msg)
        os.system("python3 GUI_functions/select_f90_GUI.py")
    def cpp_settings(self, msg):
        os.system("python3 GUI_functions/select_cpp_GUI.py")
        print(msg)
    def c_settings(self, msg):
        os.system("python3 GUI_functions/select_c_GUI.py")
        print(msg)
    def asm_settings(self, msg):
        os.system("python3 GUI_functions/select_asm_GUI.py")
        print(msg)
    
    def click_change_up(self, costs, a, machines):
        cost_value = int(costs[a][1])
        cost_value = cost_value + 1
        costs[a][1] = str(cost_value) 
        tk.Button(self.scrollFrame.viewPort, text="Thread Cost: " + costs[a][1]).grid(row=a+9+len(machines), column=2)
        tk.Button(self.scrollFrame.viewPort, text="Decrease Cost", command=lambda x=a: self.click_change_down(costs, x, machines)).grid(row=a+9+len(machines), column=3)
    
    def click_change_down(self, costs, a, machines):
        cost_value = int(costs[a][1])
        if(cost_value > 1):
            cost_value = cost_value - 1
            costs[a][1] = str(cost_value) 
            tk.Button(self.scrollFrame.viewPort, text="Thread Cost: " + costs[a][1]).grid(row=a+9+len(machines), column=2)
        else:
            tk.Button(self.scrollFrame.viewPort, text="Decrease Coss", state='disabled').grid(row=a+9+len(machines), column=3)
    
    def update_cost(self, msg):
        print(msg)
        input_file = open("GUI_functions/Tasks_details.bin", "rb")
        all_tasks= list(pickle.load(input_file))
        input_file.close()
        print("_________________")
        for j in range(len(all_tasks)):
            print(all_tasks[j])
        print("_________________")
        for i in range(len(msg)):
            for j in range(len(all_tasks)):
                if msg[i][0] == all_tasks[j][0]:
                    all_tasks[j][4] = msg[i][1]
                    break
        for j in range(len(all_tasks)):
            print(all_tasks[j])
        print("_________________")
        output_file = open("GUI_functions/Tasks_details.bin", "wb")
        pickle.dump(all_tasks, output_file)
        output_file.close()

    def printMsg_kill(self, msg):
        print(msg)
        for i in range(len(msg)):
            print(msg[i])
        root.quit()
        



if __name__ == "__main__":

    root=tk.Tk()
    root.title('Select a Machine')
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
