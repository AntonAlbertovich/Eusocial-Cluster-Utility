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

        mypath = os.path.dirname(os.path.realpath(__file__))
        mypath = mypath+"/Tasks"

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
            tk.Checkbutton(self.scrollFrame.viewPort, text= str(this_machine[0]) + " Is Connected to " + machines[row][0], relief="solid",command=lambda x=a:self.add_remove(machines[x], chosen_machines), width=40).grid(row=row, column=0)


        tk.Button(self.scrollFrame.viewPort, text="Done", command=lambda x=a: self.printMsg_kill(chosen_machines)).grid(row=row +1, column=0)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
    
    def add_remove(self, msg, chosen_programs):
        viable_add = True
        for i in range(len(chosen_programs)):
            print(str(msg[1]) +" = "+ str(chosen_programs[i]))
            if msg[1] == chosen_programs[i]:
                chosen_programs.remove(chosen_programs[i])
                viable_add = False
                break
        if (viable_add == True):
            chosen_programs.append(msg[1])
    
    def printMsg_kill(self, msg):
        print(msg)
        output_file= open("GUI_functions/update.bin", "wb")
        pickle.dump(msg, output_file)
        output_file.close()
        
        for i in range(len(msg)):
            print(msg[i])
        root_net.quit()
    
if __name__ == "__main__":

    root_net=tk.Tk()
    root_net.title('Select program dependencies')
    Example_net(root_net).pack(side="top", fill="both", expand=True)
    root_net.mainloop()
