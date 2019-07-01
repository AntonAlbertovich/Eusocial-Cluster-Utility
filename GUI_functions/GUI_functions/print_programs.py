import tkinter as tk

from tkinter import *
from os import walk
import os
from os import listdir
from os.path import isfile, join
import pickle

class ScrollFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent) 

        self.canvas = tk.Canvas(self, width = 1200, height = 800, borderwidth=0, background="black")          #place canvas on self
        self.viewPort = tk.Frame(self.canvas, width = 325, height = 300, background="black")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview) #place a scrollbar on self 
        self.hsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview) #place a scrollbar on self 
        self.canvas.configure(yscrollcommand=self.vsb.set)                          #attach scrollbar action to scroll of canvas
        self.canvas.configure(xscrollcommand=self.hsb.set)                          #attach scrollbar action to scroll of canvas
        
        self.vsb.pack(side="right", fill="y")                                       #pack scrollbar to right of self
        self.canvas.pack(side="left", fill="both", expand=True)                     #pack canvas to left of self and expand to fil
        self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",            #add view port frame to canvas
                                  tags="self.viewPort")

        self.hsb.pack(side="bottom", fill="y")                                       #pack scrollbar to right of self
        self.canvas.pack(side="top", fill="both", expand=True)                     #pack canvas to left of self and expand to fil
        self.canvas.create_window((5,5), window=self.viewPort, anchor="nw",            #add view port frame to canvas
                                  tags="self.viewPort")
        
        self.viewPort.bind("<Configure>", self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.

    def onFrameConfigure(self, event):                                              
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.



class Example_net(tk.Frame):
    
    def __init__(self, root_net):

        tk.Frame.__init__(self, root_net)
        self.scrollFrame = ScrollFrame(self) # add a new scrollable frame.
        input_file= open("GUI_functions/Tasks_details.bin", "rb")
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
    root_net.title('All Machines')
    Example_net(root_net).pack(side="top", fill="both", expand=True)
    root_net.mainloop()
