import tkinter
from tkinter import messagebox
from tkinter import font
from tkinter import *
import pickle
import os

# This script will build a GUI displaying a successfully solved answer set for a generated schedule modeled on the details given elsewhere in the interface.  

input_file = open("GUI_functions/update.bin", "rb")
all_turns = list(pickle.load(input_file))
input_file.close()
turn = int(all_turns[0])
print(all_turns)
turn_title = str(turn + 1)

def go_up():
    # This function will allow for the GUI to open up another window showing only the details for the next step in the cluster. 
    all_turns[0] = turn_title
    output_file= open("GUI_functions/update.bin", "wb")
    pickle.dump(all_turns, output_file)
    output_file.close()
    top.destroy()

def go_dw():
    # This function will allow for the GUI to open up another window showing only the details for the previous step in the cluster. 
    if turn > 0:
        turn_title = str(turn - 1)
        all_turns[0] = turn_title
        output_file= open("GUI_functions/update.bin", "wb")
        pickle.dump(all_turns, output_file)
        output_file.close()
        top.destroy()


def finish():
    # This will close the schedule display GUI.
    all_turns[0] = str(len(all_turns[1]))
    output_file= open("GUI_functions/update.bin", "wb")
    pickle.dump(all_turns, output_file)
    output_file.close()
    top.destroy()


        
#setting up
clustername = ""
username = ""
passwrd = ""
nodes = 0
tempe = 0
stemp = ""
top = tkinter.Tk()

last = 0
for i in range(len(all_turns[1])):
    this_turn = all_turns[1][i].split(",")
    this_turn[0] = this_turn[0].split("(")
    last = this_turn[2].replace(")", "")

top.title("Turn " + turn_title + " of " + last)
top.configure(bg = "black")
var = StringVar()
fnt = font.Font(family='Times', size=15, weight='bold')
label = Label(top, textvariable=var, bd = 30, relief = GROOVE, font = fnt, pady = 10, padx = 5, bg = "black", fg = "white")
var.set("Eusocial Cluster Utility")
img1 = PhotoImage(file="GUI_functions/send.gif")
img2 = PhotoImage(file="GUI_functions/run.gif")
canvas1 = Canvas(top, width = 325, height = 300, bg = "black", highlightthickness=0)
canvas1.create_image(2,2, anchor = NW, image=img1)
H = tkinter.Button(top, text ="Finish and run", font = fnt, command = finish, width = 20)
canvas2 = Canvas(top, width = 325, height = 300, bg = "black", highlightthickness=0)
canvas2.create_image(2,2, anchor = NW, image=img2)
UP = tkinter.Button(top, text ="Next Turn", font = fnt, command = go_up, width = 20)
DW = tkinter.Button(top, text ="Last Turn", font = fnt, command = go_dw, width = 20)
EN = tkinter.Button(top, text ="Exit", font = fnt, command = finish, width = 20)



canvas1.grid(row= 0, column=0)
canvas2.grid(row= 0, column=1 )
tkinter.Label(top, text="Turn "+turn_title +" Dependency Moves", relief="solid", width=60).grid(row=1, column=0)
tkinter.Label(top, text="Turn "+turn_title +" Program Executions", relief="solid", width=60).grid(row=1, column=1)
place = 0

for i in range(len(all_turns[1])):
    # Here all "moves" made in the cluster are parsed and printed to the GUI.
    this_turn = all_turns[1][i].split(",")
    this_turn[0] = this_turn[0].split("(")
    this_turn[2] = this_turn[2].replace(")", "")
    if this_turn[0][0] == "move" and this_turn[2] == turn_title:
        tkinter.Label(top, text="Program "+this_turn[0][1] + " Moved to Machine " + this_turn[1], relief="solid", width=60).grid(row=place+2, column=0)
        place = place + 1

for i in range(len(all_turns[1])):
    # Here all "executions" made in the cluster are parsed and printed to the GUI.
    this_turn = all_turns[1][i].split(",")
    this_turn[0] = this_turn[0].split("(")
    this_turn[2] = this_turn[2].replace(")", "")
    if this_turn[0][0] == "turned_at" and this_turn[2] == turn_title:
        tkinter.Label(top, text="Program "+this_turn[0][1] + " Executed on Machine " + this_turn[1], relief="solid", width=60).grid(row=place+2, column=1)
        place = place + 1

UP.grid(row = len(all_turns[1]) +3, column = 1 ) 
DW.grid(row = len(all_turns[1]) +3, column = 0 ) 
EN.grid(row = len(all_turns[1]) +4, column = 0 ) 

top.mainloop()

