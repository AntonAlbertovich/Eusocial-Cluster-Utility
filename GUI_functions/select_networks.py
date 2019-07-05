import tkinter as tk

from tkinter import *
from os import walk
import os
from os import listdir
from os.path import isfile, join
import pickle
# This script simply builds the sub-menu for the delaration of what machines a particular machine as network access to.
# A scrollable window is generated

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
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.



class menu_frame(tk.Frame):
    
    def __init__(self, root_net):

        tk.Frame.__init__(self, root_net)
        self.scrollFrame = ScrollFrame(self) # add a new scrollable frame.

        mypath = os.path.dirname(os.path.realpath(__file__))
        mypath.replace("/GUI_functions","/Tasks")

        possible_programs = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        chosen_machines = [] 
        programs = []
        input_file= open("GUI_functions/Cluster_details.bin", "rb")
        machines = pickle.load(input_file)
        input_file.close()
        
        input_file= open("GUI_functions/update.bin", "rb")
        this_machine = pickle.load(input_file)
        input_file.close()
        

        for i in range(len(machines)):
            if str(machines[i][1]) == str(this_machine[1]):
                machines.remove(machines[i])
                break

        for row in range(len(machines)):
            a = row
            tk.Checkbutton(self.scrollFrame.viewPort, text= str(this_machine[0]) + " Has Access to " + machines[row][0], relief="solid",command=lambda x=a:self.add_remove(machines[x], chosen_machines), width=40).grid(row=row, column=0)


        tk.Button(self.scrollFrame.viewPort, text="Done", command=lambda x=a: self.printMsg_kill(chosen_machines)).grid(row=row +1, column=0)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
    
    def add_remove(self, msg, chosen_programs):
        viable_add = True
        for i in range(len(chosen_programs)):
            if msg[1] == chosen_programs[i]:
                chosen_programs.remove(chosen_programs[i])
                viable_add = False
                break
        if (viable_add == True):
            chosen_programs.append(msg[0])
    
    def printMsg_kill(self, msg):
        if msg != []:
            output_file= open("GUI_functions/update.bin", "wb")
            pickle.dump(msg, output_file)
            output_file.close()
        
        root_net.quit()
    
if __name__ == "__main__":

    root_net=tk.Tk()
    root_net.title('Cluster Network')
    menu_frame(root_net).pack(side="top", fill="both", expand=True)
    root_net.mainloop()
