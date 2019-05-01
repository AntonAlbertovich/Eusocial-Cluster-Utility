import os
import pickle
#By Anton Rakos
# These are isolated methods from distributed_ledger_functions. 
# See distributed_ledger_functions.py for more specific comments
class Nodes_Macs:
    def __init__(self, node, mac):
        self.node = node
        self.mac = mac



def unique_check(list_nodes, list_macs):

    # intilize a null list 
    unique_nodes = []
    unique_macs = []
    output_list = []
    # traverse for all elements 
    for x in range(0, len(list_nodes)):
        # check if exists in unique_list or not 
        if ((list_nodes[x] not in unique_nodes) and (list_macs[x] not in unique_macs)):
            unique_nodes.append(list_nodes[x])
            unique_macs.append(list_macs[x])
            n_m = Nodes_Macs(list_nodes[x], list_macs[x])
            output_list.append(n_m)
        else:
            print("Warning, a duplicate Node name or Mac address has been detected!")
            print("Node: ", list_nodes[x], " at Address: ", list_macs[x], "will not be used.")

    return output_list


file = open("nodes.txt", "r")
Nodes = []
inets = []
dir_path = os.path.dirname(os.path.realpath(__file__))
for line in file:
    if(line[0] == "%"):
        new_node = line[1:].rstrip(' \n')
        Nodes.append(new_node)
    elif(line[0] == "m"):
        new_inet = line[1:].rstrip(' \n')
        inets.append(new_inet)
file.close()
if(len(Nodes) == len(inets)):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cluster_members = unique_check(Nodes, inets)
    for machine in cluster_members:
        command_0 = dir_path+"/"+ machine.node
        os.chdir(command_0)
        os.system("python3 view_this_dl.py")
        
        input_file = open("distributed_ledger.bin", "rb")
        distributed_public_ledger = pickle.load(input_file)
        for i in range(0, len(distributed_public_ledger)):
            this_block = distributed_public_ledger[i]
            print("----------------------------")
            print(this_block.timestamp)
            print("------------")
            print(this_block.previous_hash)
            print("------------")
            print(this_block.hash)
            print("------------")
            print(this_block.data)
        input_file.close()

        
        os.chdir(dir_path)
