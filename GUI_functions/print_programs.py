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

        self.canvas = tk.Canvas(self, width = 1200, height = 800, borderwidth=0, background="black")      
        self.viewPort = tk.Frame(self.canvas, width = 325, height = 300, background="black")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview) 
        self.hsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)  
        self.canvas.configure(yscrollcommand=self.vsb.set)                          
        self.canvas.configure(xscrollcommand=self.hsb.set)                          
        
        self.vsb.pack(side="right", fill="y")                                       
        self.canvas.pack(side="left", fill="both", expand=True)                     
        self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",tags="self.viewPort")

        self.hsb.pack(side="bottom", fill="y")                                      
        self.canvas.pack(side="top", fill="both", expand=True)                     
        self.canvas.create_window((5,5), window=self.viewPort, anchor="nw",tags="self.viewPort")
        
        self.viewPort.bind("<Configure>", self.onFrameConfigure)                       

    def onFrameConfigure(self, event):                                              
        self.canvas.configure(scrollregion=self.canvas.bbox("all")) 



class Example_net(tk.Frame):
    #This class is the main frame for this part of the menu        

    def __init__(self, root_net):

        tk.Frame.__init__(self, root_net)
        self.scrollFrame = ScrollFrame(self) # add a new scrollable frame.
        input_file= open("GUI_functions/Tasks_details.bin", "rb")
        # Here the details pertaining to the tasks of the cluster are loaeded.
        all_tasks= list(pickle.load(input_file))
        input_file.close()
        tk.Label(self.scrollFrame.viewPort, text="Program Name", relief="solid").grid(row= 0, column=0)
        tk.Label(self.scrollFrame.viewPort, text="OS needed", relief="solid").grid(row= 0, column=1)
        tk.Label(self.scrollFrame.viewPort, text="Program Dependencies", relief="solid").grid(row= 0, column=2)
        tk.Label(self.scrollFrame.viewPort, text="Toolkit Dependencies", relief="solid").grid(row= 0, column=3)
        tk.Label(self.scrollFrame.viewPort, text="Thread Cost", relief="solid").grid(row= 0, column=4)
        for i in range(len(all_tasks)):
            tk.Label(self.scrollFrame.viewPort, text=all_tasks[i][0], relief="solid").grid(row= i+1, column=0)
            tk.Label(self.scrollFrame.viewPort, text=all_tasks[i][1][1], relief="solid").grid(row= i+1, column=1)
            tk.Label(self.scrollFrame.viewPort, text=all_tasks[i][2], relief="solid").grid(row= i+1, column=2)
            tk.Label(self.scrollFrame.viewPort, text=all_tasks[i][3], relief="solid").grid(row= i+1, column=3)
            tk.Label(self.scrollFrame.viewPort, text=all_tasks[i][4], relief="solid").grid(row= i+1, column=4)

        tk.Button(self.scrollFrame.viewPort, text="Done", command=lambda x=0: self.printMsg_kill("a")).grid(row=len(all_tasks) +1, column=0)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
    
    
    def printMsg_kill(self, msg):
        root_net.quit()
    
if __name__ == "__main__":

    root_net=tk.Tk()
    root_net.title('All Programs')
    Example_net(root_net).pack(side="top", fill="both", expand=True)
    root_net.mainloop()
