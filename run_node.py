import os
import socket
import time
from distributed_ledger_functions import create_genesis_block
from distributed_ledger_functions import next_block
from cpu_temptest import monitor_cluster_node_high_cpu_temp
dir_path = os.path.dirname(os.path.realpath(__file__))
cluster_name = "Eusocial-Cluster" #n
user_name = "user" #u
user_pass = "root" #p
node_name = "Node" #v
max_temperature = 90 #t
job_interval = 5 #i
job_time = 1 #c
Nodes = []
inets = []
print(dir_path)
os.system(" ls")
in_line = open("info.txt", "r")
for line in in_line:
    if(line[0] == "n"):
        cluster_name = line[1:].rstrip(' \n')
    elif(line[0] == "u"):
        user_name = line[1:].rstrip(' \n')
    elif(line[0] == "p"):
        user_pass = line[1:].rstrip(' \n')
    elif(line[0] == "v"):
        node_name = line[1:].rstrip(' \n')
    elif(line[0] == "t"):
        max_temperature = line[1:].rstrip(' \n')
    elif(line[0] == "i"):
        job_interval = line[1:].rstrip(' \n')
    elif(line[0] == "c"):
        job_time = line[1:].rstrip(' \n')
in_line.close()
file = open("nodes.txt", "r")
for line in file:
    if(line[0] == "m"):
        new_inet = line[1:].rstrip(' \n')
        inets.append(new_inet)
file.close()
name = socket.gethostname()
closing_time = time.time() +60*60*float(job_time)
while time.time() < closing_time:
    print("Phase I")
    thermal_data = monitor_cluster_node_high_cpu_temp(name, job_interval)
    print("Phase II")
    for mac in inets:
        print("Phase III")
        command_1 = "sshpass -p'"+ user_pass + "' ssh " + user_name + "@" + mac + " rm " +cluster_name + "/distributed_ledger.bin"
        command_2 = "sshpass -p'"+ user_pass + "' scp "+dir_path+"/distributed_ledger.bin"+" " + user_name + "@" + mac +":/home/"+user_name+"/"+cluster_name
        print("Phase IIII")
        try:
            os.system(command_1)
            print(command_1)
        except:
            print("Error on command: ", command_1)
        try:
            os.system(command_2)
            print(command_2)
        except:
            print("Error on command: ", command_2)
    print("Phase V")

print("Phase VI")

