import os 
from multiprocessing import Process  
def func0():
    command_0 = "sshpass -p'root'  ssh user@192.168.1.00 python3.7 Eusocial-Cluster/run_node.py " 
    try: 
        os.system(command_0)
    except: 
        print('Error: on command_0 in sub function 0 ')
def func1():
    command_0 = "sshpass -p'root'  ssh user@192.168.1.01 python3.7 Eusocial-Cluster/run_node.py " 
    try: 
        os.system(command_0)
    except: 
        print('Error: on command_0 in sub function 1 ')
def func2():
    command_0 = "sshpass -p'root'  ssh user@192.168.1.02 python3.7 Eusocial-Cluster/run_node.py " 
    try: 
        os.system(command_0)
    except: 
        print('Error: on command_0 in sub function 2 ')
def func3():
    command_0 = "sshpass -p'root'  ssh user@192.168.1.05 python3.7 Eusocial-Cluster/run_node.py " 
    try: 
        os.system(command_0)
    except: 
        print('Error: on command_0 in sub function 3 ')
if __name__=='__main__': 
    p0 = Process(target = func0)
    p0.start()
    p1 = Process(target = func1)
    p1.start()
    p2 = Process(target = func2)
    p2.start()
    p3 = Process(target = func3)
    p3.start()
