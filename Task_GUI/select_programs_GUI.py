import tkinter as tk

from tkinter import *
from os import walk
import os
from os import listdir
from os.path import isfile, join
# ************************
# Scrollable Frame Class
# ************************
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


# ********************************
# Example usage of the above class
# ********************************

class Example(tk.Frame):
    
    def __init__(self, root):

        tk.Frame.__init__(self, root)
        self.scrollFrame = ScrollFrame(self) # add a new scrollable frame.

        mypath = os.path.dirname(os.path.realpath(__file__))

        possible_programs = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        chosen_programs = [] 
        programs = []
        for i in possible_programs:
            if ".py" in i:
                programs.append(i)
            if ".swp" in i:
                programs.remove(i)

        for row in range(len(programs)):
            a = row
            tk.Checkbutton(self.scrollFrame.viewPort, text= "Files produced by: " + programs[row], width=35, relief="solid",command=lambda x=a:
                    self.add_remove(str(programs[x]), chosen_programs)).grid(row=row, column=0)
                    

        tk.Button(self.scrollFrame.viewPort, text="Done", command=lambda x=a: self.printMsg_kill(chosen_programs)).grid(row=row +1, column=0)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
    
    def add_remove(self, msg, chosen_programs):
        viable_add = True
        for i in range(len(chosen_programs)):
            if msg == chosen_programs[i]:
                chosen_programs.remove(chosen_programs[i])
                viable_add = False
                break
        if (viable_add == True):
            chosen_programs.append(msg)
    
    def printMsg_kill(self, msg):
        print(msg)
        for i in range(len(msg)):
            print(msg[i])
        root.quit()
    
if __name__ == "__main__":

    root=tk.Tk()
    root.title('Select program dependencies')
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
