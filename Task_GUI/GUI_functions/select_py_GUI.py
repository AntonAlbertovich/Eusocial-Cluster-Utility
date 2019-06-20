import tkinter as tk

from tkinter import *
from os import walk
import os
from os import listdir
from os.path import isfile, join
import pickle

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

        
        chosen_programs = [] 
        programs = []
        
        input_file = open("GUI_functions/Tasks_details.bin", "rb")
        possible_programs = pickle.load(input_file)
        input_file.close()
        
        for i in range(len(possible_programs)):
            if ".py" in possible_programs[i][0]:
                programs.append(possible_programs[i])
            if ".swp" in possible_programs[i][0]:
                programs.remove(possible_programs[i])

        for row in range(len(programs)):
            a = row
            tk.Checkbutton(self.scrollFrame.viewPort, text= "Settings for: " + programs[row][0], width=35, relief="solid",command=lambda x=a: self.add_remove(programs[x], chosen_programs)).grid(row=row, column=0)
                    

        tk.Button(self.scrollFrame.viewPort, text="Save and Update Settings", command=lambda x=a: self.printMsg_kill(chosen_programs)).grid(row=row +1, column=0)
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
            os.system("python3 GUI_functions/select_depend.py")
            input_file = open("GUI_functions/update.bin", "rb")
            new_task = pickle.load(input_file)
            input_file.close()
            chosen_programs.append(new_task)
            print(new_task)
            print(chosen_programs)

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
    root.title('Select Python Dependecies')
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
