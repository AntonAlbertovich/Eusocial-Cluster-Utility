import tkinter as tk

from tkinter import *
from os import walk
import os
from os import listdir
from os.path import isfile, join
import pickle

# This script simply builds the sub-menu for all python programs.
# A scrollable window is generated
# When a program is selected then the universal depenecies sub-menu is open via select_depend.py
# Once the edits have been made to the universal depenecies sub-menu the user may update the task detials data structure via clicking the button: "Save and Update Settings"


class ScrollFrame(tk.Frame):
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
        self.canvas.configure(scrollregion=self.canvas.bbox("all")) 



class sub_menu(tk.Frame):
    
    def __init__(self, root):

        tk.Frame.__init__(self, root)
        self.scrollFrame = ScrollFrame(self) # add a new scrollable frame.

        chosen_programs = []
        programs = []
        
        input_file = open("GUI_functions/Tasks_details.bin", "rb")
        possible_programs = pickle.load(input_file)
        input_file.close()

        for i in range(len(possible_programs)):
            if ".py" in possible_programs[i][0]:
                programs.append(possible_programs[i])

        for row in range(len(programs)):
            a = row
            tk.Checkbutton(self.scrollFrame.viewPort, text= "Execution Conditions for: " + programs[row][0], width=35, relief="solid",command=lambda x=a: self.add_remove(programs[x], chosen_programs)).grid(row=row, column=0)


        tk.Button(self.scrollFrame.viewPort, text="Save and Update Execution Settings", command = lambda x=1: self.printMsg_kill(chosen_programs)).grid(row=len(programs) +1, column=0)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
    
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
            os.system("python3 GUI_functions/select_exe.py")
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
    
if __name__ == "__main__":

    root=tk.Tk()
    root.title('Python Program')
    sub_menu(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
