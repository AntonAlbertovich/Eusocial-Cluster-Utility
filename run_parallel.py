import os 
from multiprocessing import Process  
def func0():
    command_0 = "sshpass -p'root'  ssh user@000 python3.7 Eusocial-Cluster/run_node.py " 
    try: 
        os.system(command_0)
    except: 
        print('Error: on command_0 in sub function 0 ')
def func1():
    command_0 = "sshpass -p'root'  ssh user@001 python3.7 Eusocial-Cluster/run_node.py " 
    try: 
        os.system(command_0)
    except: 
        print('Error: on command_0 in sub function 1 ')
def func2():
    command_0 = "sshpass -p'root'  ssh user@002 python3.7 Eusocial-Cluster/run_node.py " 
    try: 
        os.system(command_0)
    except: 
        print('Error: on command_0 in sub function 2 ')
if __name__=='__main__': 
    p0 = Process(target = func0)
    p0.start()
    p1 = Process(target = func1)
    p1.start()
    p2 = Process(target = func2)
    p2.start()
