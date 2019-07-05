import tkinter as tk

from tkinter import *
from os import walk
import os
from os import listdir
from os.path import isfile, join
import pickle

class ScrollFrame(tk.Frame):
    # This class allows for a frame which can be scrolled vertically.
    # This is very need as a given cluster may contain many machines or be tasked with many jobs.

    def __init__(self, parent):
        super().__init__(parent) 

    
        self.canvas = tk.Canvas(self, borderwidth=0, background="black")
        self.viewPort = tk.Frame(self.canvas, background="black")       
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview) #place a scrollbar on self 
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")             
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",tags="self.viewPort")
        self.viewPort.bind("<Configure>", self.onFrameConfigure)

    def onFrameConfigure(self, event):                                              
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 



class Example_net(tk.Frame):
    
    def __init__(self, root_net):

        tk.Frame.__init__(self, root_net)
        self.scrollFrame = ScrollFrame(self) 

        toolkits = ["CUDA", "spaCy", "psutil", "clingo"]
        chosen_toolkits = []
        input_file= open("GUI_functions/update.bin", "rb")
        this_machine = pickle.load(input_file)
        input_file.close()
        

        for row in range(len(toolkits)):
            a = row
            tk.Checkbutton(self.scrollFrame.viewPort, text= str(this_machine[0]) + " has installed  " + toolkits[row], relief="solid",command=lambda x=a:self.add_remove(toolkits[x], chosen_toolkits), width=40).grid(row=row, column=0)


        tk.Button(self.scrollFrame.viewPort, text="Done", command=lambda x=a: self.printMsg_kill(chosen_toolkits)).grid(row=row +1, column=0)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
    
    def add_remove(self, msg, chosen_toolkits):
        viable_add = True
        for i in range(len(chosen_toolkits)):
            if msg == chosen_toolkits[i]:
                chosen_toolkits.remove(chosen_toolkits[i])
                viable_add = False
                break
        if (viable_add == True):
            chosen_toolkits.append(msg)
    
    def printMsg_kill(self, msg):
        if msg != []:
            output_file= open("GUI_functions/update.bin", "wb")
            pickle.dump(msg, output_file)
            output_file.close()
        
        root_net.quit()
    
if __name__ == "__main__":

    root_net=tk.Tk()
    root_net.title('Select Dependency Toolkits')
    Example_net(root_net).pack(side="top", fill="both", expand=True)
    root_net.mainloop()
