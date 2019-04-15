from  distributed_ledger_functions import verify_distributed_public_ledger 
import os

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
        try:
            os.chdir(command_0)
            boolean = verify_distributed_public_ledger()
            if(boolean == False):
                print(machine.node, " public ledger compromised, tampering was detected.")
            elif(boolean == True):
                print(machine.node, " public ledger integrity confirmed, no tampering detected.")
            os.chdir(dir_path)
        except:
            print("Error on command: ", command_3)

