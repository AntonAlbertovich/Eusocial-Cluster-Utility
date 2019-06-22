import tkinter
from tkinter import messagebox
from tkinter import font
from tkinter import *
import pickle
import os
#setting up
clustername = ""
username = ""
passwrd = ""
nodes = 0
tempe = 0
stemp = ""
top = tkinter.Tk()
top.title("ECU")
top.configure(bg = "black")
# Code to add widgets will go here...
var = StringVar()
fnt = font.Font(family='Times', size=15, weight='bold')
label = Label(top, textvariable=var, bd = 30, relief = GROOVE, font = fnt, pady = 10, padx = 5, bg = "black", fg = "white")
var.set("Eusocial Cluster Utility")
img = PhotoImage(file="light.gif")
canvas = Canvas(top, width = 325, height = 300, bg = "black", highlightthickness=0)
canvas.create_image(2,2, anchor = NW, image=img)
#functions for each button

#this function displays the instructions for first time use
def first():
   messagebox.showinfo( "Instructions for first time use", "Please install the following dependencies before " +
    "using!\n 1.)Openssh-server \n 2.)cssh \n 3.)gfortran \n\nPlease fill out all information, as all fields will be necessary. " +
    "\nYou will need to repeat the add node step for every node, including the steps for finding each MAC address.")
#this function contains the code for the add node option/widget
def addnode():
    messagebox.showinfo("Add node",
                        "Please enter the name of the new node. \nNote that this should be the name of the machine " +
                        "and not the uniform node title.")
    messagebox.showinfo("Enter MAC address",
                        "You will also need to enter the node's MAC address. \nTo find MAC address: \n" + "1.) Open a terminal. \n2.) Type in \"ifconfig -a\" without quotes and hit enter." +
                        "\n3.) The returned value is the MAC address, copy and paste it in the next box.")
    txt = tkinter.Tk()
    v = StringVar()
    w = StringVar()
    E1 = Entry(txt, bd=5, textvariable=v)
    E2 = Entry(txt, bd=5, textvariable=w)
    E1.grid()
    E1.focus_set()
    file = open("nodes.txt", "a")
    file.write("##################\n")
    file.close()
   #this function takes a node name
    new_machine = []
    new_machine.append("name")
    new_machine.append("0.0")
    new_machine.append(0)
    
    def add():
        new_machine[0] = E1.get()
        E1.destroy()
        button.destroy()
    #this function takes a MAC address
    def setmac():
        new_machine[1] = E2.get()
        E2.destroy()
        button2.destroy()
    #asks whether the node has a gpu
    def gpu():
        def yes():
            new_machine[2] = 1
            ex.destroy()
            button4.destroy()
        def no():
            new_machine[2] = 0
            ex.destroy()
            button4.destroy()
        ex = tkinter.Tk()
        but = Button(ex, text="Yes", width=5, command=yes)
        but1 = Button(ex, text="No", width=5, command=no)
        label = Label(ex, text="Does this node have a GPU with Nvidia CUDA 10.0 and NVCC toolkit support?", bd=30)
        label.grid()
        but.grid()
        but1.grid()
    #saves the entered data and exits
    def exit():
        print(new_machine)
        if len(new_machine) == 3:
            
            file = open("nodes.txt", "a")
            #when adding a new node, it will start with a pound sign as an identifier
            file.write("%"  + new_machine[0] + "\n")
            
            # when adding a new node, GPU uses a g as identifier

            file.write("m" + new_machine[1] + "\n")
            
            file = open("nodes.txt", "a")
            # when adding a new node, GPU uses a g as identifier
            if new_machine[2] == 1:
                file.write("gyes" + "\n")
            else:
                file.write("gno" + "\n")
           
            input_file= open("GUI_functions/Cluster_details.bin", "rb")
            all_tasks= list(pickle.load(input_file))
            input_file.close()
            for i in range(len(all_tasks)):
                #searching by MAC address, not machines name
                if new_machine[1] == all_tasks[i][1]:
                    all_tasks.remove(all_tasks[i])
                    print("A double was deleted")
                    break
            viable_machine = []
            Machine_Netwk=[]
            Machine_tools=[]
            Machine_hours=[]
            Machine_Processor_count=4


            viable_machine.append(new_machine[0])       #This can be later cleaned up as new_machine[2] is not used
            viable_machine.append(new_machine[1])       #new_machine[2] is true or false if the machine has a GPU, but knowing this may not be needed 
            viable_machine.append(Machine_Netwk)        
            viable_machine.append(Machine_tools)
            viable_machine.append(Machine_hours)
            viable_machine.append(["python3 ", "gfortran ", "gcc ", "g++", "nasm -felf64 "])
            viable_machine.append(Machine_Processor_count)
            viable_machine.append("Ubuntu 18.04 [Desktop Edition]")
            #print(viable_machine)
            all_tasks.append(viable_machine)
            
            print(all_tasks)
            for i in range(len(all_tasks)):
                print("---------------") 
                print(all_tasks[i])
            output_file = open("Task_GUI/GUI_functions/Cluster_details.bin", "wb")
            pickle.dump(all_tasks, output_file)
            output_file.close()



            all_tasks.append(new_machine) 



            
            file.close()

        txt.destroy()
    button = Button(txt, text="Set node name", width=20, command=add)
    button2 = Button(txt, text ="Set MAC address", width=20, command=setmac)
    button3 = Button(txt, text="Exit", width=20, command=exit)
    button4 = Button(txt, text = "GPU support", width=20, command=gpu)
    button.grid()
    E2.grid()
    button2.grid()
    button4.grid()
    button3.grid()
    txt.mainloop()
#this function contains the code for storing the username in a text file
def build_schedule():
    os.system("python3 configuring_menu.py")
    print("e")

def user():
    messagebox.showinfo("Enter username",
                        "Make sure there is a profile on each computer with administrative priveleges " +
                        "under the username you are about to enter")
    txt = tkinter.Tk()
    txt.configure(width = 30)
    v = StringVar()
    E1 = Entry(txt, bd=5, textvariable=v)
    E1.grid()
    E1.focus_set()
    def username():
        username = E1.get()
        file = open("info.txt", "a")
        #the username line begins with a u as an identifier
        file.write("u" + username + "\n")
        file.close()
        txt.destroy()
    button = Button(txt, text="Set username", width=10, command=username)
    button.grid()
    txt.mainloop()
#this saves the entered info in the text file
def setname():
    txt = tkinter.Tk()
    v = StringVar()
    E1 = Entry(txt, bd=5, textvariable = v)
    E1.grid()
    E1.focus_set()
    def setclus():
        clustername = E1.get()
        file = open("info.txt", "a")
        #the cluster name line begins with an n as an identifier
        file.write("n" + clustername + "\n")
        file.close()
        txt.destroy()
    button = Button(txt, text="Set name", width=10, command=setclus)
    button.grid()
    txt.mainloop()
#this function contains the code for storing the node title in a text file
def setnodename():
    messagebox.showinfo("Enter node title","The title you enter will have a number appended to it to keep all " +
                                  "node titles uniform. \n(e.g. Unit001, Unit002, etc.)")
    txt = tkinter.Tk()
    v = StringVar()
    E1 = Entry(txt, bd=5, textvariable = v)
    E1.grid()
    E1.focus_set()
    def nodename():
        nod = E1.get()
        file = open("info.txt", "a")
        #the node name uses a u as an identifier
        file.write("v" + nod + "\n")
        file.close()
        txt.destroy()
    button = Button(txt, text="Set node title", width=10, command=nodename)
    button.grid()
    txt.mainloop()
#this function contains the code for storing the password in a text file
def setpass():
    messagebox.showinfo("Enter ssh password", "Make sure the password you enter is the administrative password for all nodes in the cluster.")
    txt = tkinter.Tk()
    v = StringVar()
    E1 = Entry(txt, bd=5, textvariable = v, show ="*")
    E1.grid()
    E1.focus_set()
    def password():
        passwrd = E1.get()
        #print (passwrd)
        file = open("info.txt","a")
        #the password line begins with a p as an identifier
        file.write("p" + passwrd + "\n")
        file.close()
        txt.destroy()
    button = Button(txt, text="Set password", width=10, command=password)
    button.grid()
    txt.mainloop()
#this function contains the code for reseting the text file and clearing the data
def reset():
    txt = tkinter.Tk()
    txt.title("Create new cluster")
    label = Label(txt, text = "Warning: This will clear previous cluster data.", bd = 30)
    label.pack()
    def clear():
        new_machines = []
        output_file = open("Task_GUI/GUI_functions/Cluster_details.bin", "wb")
        pickle.dump(new_machines, output_file)
        output_file.close()
        file = open("info.txt", "w")
        file.close()
        file = open("nodes.txt", "w")
        file.close()
        nodes = 0
        username = ""
        passwrd = ""
        clustername = ""
        messagebox.showinfo("Create new cluster", "Previous data has been cleared.")
        txt.destroy()
    button = Button(txt, text="Clear data", width=10, command=clear)
    button.pack()
    txt.mainloop()
#this closes the gui
def finish():
    top.destroy()
#this function contains the code for storing the maximum temperature setting in the text file
def temp():
    messagebox.showinfo("Enter max CPU temp","Set the temperature limit for all machines across the cluster. It is recommended that you choose a temperature between 90 to 105 degrees. "
                                             +"Setting a temperature below 50 degrees or above 120 degrees will result in an error.")
    txt = tkinter.Tk()
    v = StringVar()
    E1 = Entry(txt, bd=5, textvariable = v)
    E1.grid()
    E1.focus_set()
    def settemp():
        tempe = int(E1.get())
        stemp = E1.get()
        print(E1.get())
        if int(E1.get()) <= 120:
            if int(E1.get()) >= 50:
                file = open("info.txt", "a")
                #the temperature uses a t as an identifier
                file.write("t" + stemp + "\n")
                file.close()
                txt.destroy()
            else:
                messagebox.showerror("Error", "Please choose a number between 50 and 120.")
                txt.destroy()
        else:
            messagebox.showerror("Error", "Please choose a number between 50 and 120.")
            txt.destroy()
    button = Button(txt, text="Set CPU temp(°C)", width=20, command=settemp)
    button.grid()
    txt.mainloop()
#this function stores the entered test interval information in the text file.
def test():
    messagebox.showinfo("Set test interval","This will set how often data will be sampled across the cluster.  ECU will "
                                            +"survey the hardware in each machine once per number of minutes entered. "
                                             +"At the end of this period the collected data will be sent to the distributed "
                                              +"public ledger on all machines. Only intervals between once a minute and once per 60 minutes will be accepted.")
    txt = tkinter.Tk()
    v = StringVar()
    E1 = Entry(txt, bd=5, textvariable = v)
    E1.grid()
    E1.focus_set()
    def setint():
        stemp = E1.get()
        print(E1.get())
        if int(E1.get()) <= 60:
            if int(E1.get()) >= 1:
                file = open("info.txt", "a")
                #the interval uses a i as an identifier
                file.write("i" + stemp + "\n")
                file.close()
                txt.destroy()
            else:
                messagebox.showerror("Error", "Please choose a number between 1 and 60.")
                txt.destroy()
        else:
            messagebox.showerror("Error", "Please choose a number between 1 and 60.")
            txt.destroy()
    button = Button(txt, text="Set interval", width=10, command=setint)
    button.grid()
    txt.mainloop()
#this function stores the job time information in the text file
def jobtime():
    messagebox.showinfo("Set job time","This will set how long data will be sampled across the cluster.  "
                                       +"ECU will survey the hardware throughout the cluster for  up to 96 hours.  "
                                        +"The minimum Job Time is 1 hour.  Rebooting  during the Set Job Time will "
                                         +"result in failure to complete the test.")
    txt = tkinter.Tk()
    v = StringVar()
    E1 = Entry(txt, bd=5, textvariable = v)
    E1.grid()
    E1.focus_set()
    def jobt():
        stime = E1.get()
        print(E1.get())
        if int(E1.get()) <= 96:
            if int(E1.get()) >= 1:
                file = open("info.txt", "a")
                #the time uses a c as an identifier
                file.write("c" + stime + "\n")
                file.close()
                txt.destroy()
            else:
                messagebox.showerror("Error", "Please choose a number between 1 and 96.")
                txt.destroy()
        else:
            messagebox.showerror("Error", "Please choose a number between 1 and 96.")
            txt.destroy()
    button = Button(txt, text="Set job time", width=10, command=jobt)
    button.grid()
    txt.mainloop()

#putting widgets in order
pad1 = tkinter.Frame(top, width=600, height=45, bg = "black")
pad2 = tkinter.Frame(top, width=350, height=45, bg = "black")
pad3 = tkinter.Frame(top, width=350, height=45, bg = "black")
pad4 = tkinter.Frame(top, width=350, height=20, bg = "black")
pad5 = tkinter.Frame(top, width=350, height=20, bg = "black")
fnt = font.Font(family='Times')
A = tkinter.Button(top, text ="Instructions for first time use", font = fnt,command = first, width = 20)
B = tkinter.Button(top, text ="Add node", font = fnt,command = addnode, width = 20)
C = tkinter.Button(top, text ="Set cluster name", font = fnt,command = setname, width = 20)
D = tkinter.Button(top, text ="Set username", font = fnt,command = user, width = 20)
E = tkinter.Button(top, text ="Set ssh password", font = fnt,command = setpass, width = 20)
F = tkinter.Button(top, text ="Set node title", font = fnt,command = setnodename, width = 20)
G = tkinter.Button(top, text ="Create new cluster", font = fnt,command = reset, width = 20)
H = tkinter.Button(top, text ="Finish and run", font = fnt, command = finish, width = 20)
I = tkinter.Button(top, text ="Max CPU temperature", font = fnt, command = temp, width = 20)
J = tkinter.Button(top, text ="Set testing interval", font = fnt, command = test, width = 20)
K = tkinter.Button(top, text ="Set job time", font = fnt, command = jobtime, width = 20)
L = tkinter.Button(top, text ="Build Schedule", font = fnt, command = build_schedule, width = 20)
pad3.grid()
label.grid()
canvas.grid()
A.grid()
G.grid()
B.grid()
C.grid()
D.grid()
E.grid()
F.grid()
I.grid()
J.grid()
K.grid()
L.grid()
H.grid()
pad2.grid()
top.mainloop()
