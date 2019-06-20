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

    
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.viewPort = tk.Frame(self.canvas, background="#ffffff")       
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



class Example_net(tk.Frame):
    
    def __init__(self, root_net):

        tk.Frame.__init__(self, root_net)
        self.scrollFrame = ScrollFrame(self) # add a new scrollable frame.

        toolkits = ["UTC Hour: 00:00", "UTC Hour: 01:00", "UTC Hour: 02:00", "UTC Hour: 03:00", "UTC Hour: 04:00", "UTC Hour: 05:00", "UTC Hour: 06:00", "UTC Hour: 07:00", "UTC Hour: 08:00", "UTC Hour: 09:00", "UTC Hour: 10:00", "UTC Hour: 11:00", "UTC Hour: 12:00", "UTC Hour: 13:00", "UTC Hour: 14:00", "UTC Hour: 15:00", "UTC Hour: 15:00", "UTC Hour: 16:00", "UTC Hour: 17:00", "UTC Hour: 18:00", "UTC Hour: 19:00", "UTC Hour: 20:00", "UTC Hour: 21:00", "UTC Hour: 22:00", "UTC Hour: 23:00"]
        chosen_toolkits = []
        input_file= open("GUI_functions/update.bin", "rb")
        this_machine = pickle.load(input_file)
        input_file.close()
        
        print(this_machine[1])

        for row in range(len(toolkits)):
            a = row
            tk.Checkbutton(self.scrollFrame.viewPort, text= str(this_machine[0]) + " is available at " + toolkits[row], relief="solid",command=lambda x=a:self.add_remove(toolkits[x], chosen_toolkits), width=40).grid(row=row, column=0)


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
        print(msg)
        output_file= open("GUI_functions/update.bin", "wb")
        pickle.dump(msg, output_file)
        output_file.close()
        
        root_net.quit()
    
if __name__ == "__main__":

    root_net=tk.Tk()
    root_net.title('Select hours of availablity')
    Example_net(root_net).pack(side="top", fill="both", expand=True)
    root_net.mainloop()
