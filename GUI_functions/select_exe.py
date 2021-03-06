import tkinter as tk
from tkinter import ttk
from tkinter import *
from os import walk
import os
from os import listdir
from os.path import isfile, join
import pickle


# This script simply builds the sub-menu for configuring the individual needs of any particular program in the cluster.
# A scrollable window is generated

input_file = open("GUI_functions/update.bin", "rb")
this_task = list(pickle.load(input_file))
print(this_task)
input_file.close()

input_file = open("GUI_functions/Tasks_details.bin", "rb")
all_tasks= list(pickle.load(input_file))
input_file.close()

task_loc = 0

for i in range(len(all_tasks)):
    print(this_task[0])
    if this_task[0] == all_tasks[i][0]:
        task_loc = i
        print("ping!")
        break
        



class ScrollFrame(tk.Frame):
    # This class allows for a frame which can be scrolled vertically.
    # This is very need as a given cluster may contain many machines or be tasked with many jobs.

    def __init__(self, parent):
        super().__init__(parent) 

    
        self.canvas = tk.Canvas(self, borderwidth=0, background="black")
        self.viewPort = tk.Frame(self.canvas, background="black")       
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)  
        self.canvas.configure(yscrollcommand=self.vsb.set)                          

        self.vsb.pack(side="right", fill="y")                                       
        self.canvas.pack(side="left", fill="both", expand=True)                     
        self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)

    def onFrameConfigure(self, event):                                              
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all")) 



class menu_frame(tk.Frame):
    
    def __init__(self, root):
        import os
        tk.Frame.__init__(self, root)
        self.scrollFrame = ScrollFrame(self) # add a new scrollable frame.

        chosen_programs = [] 
        programs = []
        
        input_file = open("GUI_functions/Tasks_details.bin", "rb")
        possible_programs = pickle.load(input_file)
        input_file.close()

        print(possible_programs)
        # This section will print out an organized list of all other programs in the cluster
        for i in range(len(possible_programs)):
            if ".py" in  possible_programs[i][0]:
                programs.append(possible_programs[i]) 
            if ".swp" in  possible_programs[i][0]:
                programs.remove(possible_programs[i])

        for i in range(len(possible_programs)):
            if ".c" in possible_programs[i][0]:
                programs.append(possible_programs[i])
            if ".cpp" in possible_programs[i][0]:
                programs.remove(possible_programs[i])

        for i in range(len(possible_programs)):
            if ".cpp" in possible_programs[i][0]:
                programs.append(possible_programs[i])
        
        for i in range(len(possible_programs)):
            if ".asm" in  possible_programs[i][0]:
                programs.append(possible_programs[i])
        
        for i in range(len(possible_programs)):
            if ".f90" in  possible_programs[i][0]:
                programs.append(possible_programs[i])

        for i in range(len(possible_programs)):
            if this_task[0] in possible_programs[i][0]:
                programs.remove(possible_programs[i])

        os_0_Label = ttk.Label(self.scrollFrame.viewPort, text="Select an Operating System: ", width=30)
        os_0_Label.grid(column=0, row=0)

        os_0_Label = ttk.Label(self.scrollFrame.viewPort, text="Select Programs Which Produce Dependencies: ", width=45)
        os_0_Label.grid(column=0, row=7)

        os_distor= ['Ubuntu 18.04 [Desktop Edition]', 'CentOS 7 [Desktop Edition]', 'CentOS 7 [Node/server Edition]', 'Unlisted Debian based OS', 'Unlisted Red Hat based OS', 'N/A']
        def os_Call():
            coreSel=os_Var.get()
            if coreSel == 0:
                all_tasks[task_loc][1][0] = 1
                all_tasks[task_loc][1][1] = "Ubuntu 18.04 [Desktop Edition]"
            elif coreSel == 1:
                all_tasks[task_loc][1][0] = 1
                all_tasks[task_loc][1][1] = "CentOS 7 [Desktop Edition]"
            elif coreSel == 2:
                all_tasks[task_loc][1][0] = 1
                all_tasks[task_loc][1][1] = "CentOS 7 [Node/server Edition]"
            elif coreSel == 3:
                all_tasks[task_loc][1][0] = 1
                all_tasks[task_loc][1][1] = "Unlisted Debian based OS"
            elif coreSel == 4:
                all_tasks[task_loc][1][0] = 1
                all_tasks[task_loc][1][1] = "Unlisted Red Hat based OS"
            elif coreSel == 5:
                all_tasks[task_loc][1][0] = 0
                all_tasks[task_loc][1][1] = "N/A"
        
        os_Var = tk.IntVar()

        # Next we are selecting a non-existing index value for radVar.
        os_Var.set(99)


        for row in range(len(programs)):
            a = row
            tk.Checkbutton(self.scrollFrame.viewPort, text= "Files produced by: " + programs[row][0], width=35, relief="solid",command=lambda x=a: self.add_remove(programs[x], chosen_programs)).grid(row=row+8, column=0)

                    

        toolkits = ["CUDA", "spaCy", "psutil", "clingo"]
        chosen_toolkits = []
        for row in range(len(toolkits)):
            a = row
            tk.Checkbutton(self.scrollFrame.viewPort, text = toolkits[row]+" is required", relief="solid",command=lambda x=a:self.add_remove(toolkits[x], chosen_toolkits), width=30).grid(row=row+10+len(programs), column=0)

        tk.Button(self.scrollFrame.viewPort, text="Updated File Dependencies", command=lambda x=a: self.save_prg(chosen_programs)).grid(row=len(programs) + 9, column=0)
        tk.Button(self.scrollFrame.viewPort, text="Updated Toolkit Dependencies", command=lambda x=a: self.save_tools(chosen_toolkits)).grid(row=row+11+len(programs)+len(toolkits), column=0)
        tk.Button(self.scrollFrame.viewPort, text="Done, Exit Program Settings", command=lambda x=a: self.printMsg_kill(chosen_programs)).grid(row=row+12+len(programs)+len(toolkits), column=0)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
    

    
    def add_remove(self, msg, chosen_programs):
        # this function manages the chack mark buttons, futher testing is needed to determin if this function is still needed.
        viable_add = True
        for i in range(len(chosen_programs)):
            if msg == chosen_programs[i]:
                chosen_programs.remove(chosen_programs[i])
                viable_add = False
                break
        if (viable_add == True):
            chosen_programs.append(msg)
    

    def save_prg(self, msg):
        # This updates program dependencies.
        msg_out = []
        for i in range(len(msg)):
                msg_out.append(msg[i][0])
        all_tasks[task_loc][2] = msg_out

    def save_tools(self, msg):
        # This updates toolkit dependencies.
        all_tasks[task_loc][3] = msg 

    def printMsg_kill(self, msg):
        output_file = open("GUI_functions/update.bin", "wb")
        pickle.dump(all_tasks[task_loc], output_file)
        output_file.close()
        root.quit()
    
if __name__ == "__main__":

    root=tk.Tk() 
    root.title(str(this_task[0]) + ' Execution  Settings')
    menu_frame(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
