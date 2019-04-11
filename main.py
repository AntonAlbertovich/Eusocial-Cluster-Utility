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


def build_cluster():

    # defual variables
    import os
    import socket
    from distributed_ledger_functions import create_genesis_block
    from distributed_ledger_functions import next_block
    
    
    cluster_name = "Eusocial-Cluster" #n
    user_name = "user" #u
    user_pass = "root" #p
    node_name = "Node" #v
    max_temperature = 90 #t
    job_interval = 5 #i
    job_time = 1 #c
    Nodes = [] 
    inets = []

    print(cluster_name)
    print(user_name)
    print(user_pass)
    print(node_name)
    print(max_temperature)
    print(job_interval)
    print(job_time)

    file = open("info.txt", "r")
    for line in file:
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
    print(cluster_name)
    print(user_name)
    print(user_pass)
    print(node_name)
    print(max_temperature)
    print(job_interval)
    print(job_time) 
    file.close()
    file = open("nodes.txt", "r")
    
    for line in file:
        if(line[0] == "%"):
            new_node = line[1:].rstrip(' \n')
            Nodes.append(new_node)
        elif(line[0] == "m"):
            new_inet = line[1:].rstrip(' \n')
            inets.append(new_inet)
    file.close()
    if(len(Nodes) == len(inets)):
        cluster_members = unique_check(Nodes, inets)
        numerical_designation = 0 
        create_genesis_block()
        cluster_birth_certificate = "Cluster: "+ cluster_name + "Made by: " + node_name 
        next_block(cluster_birth_certificate)
        for machine in cluster_members:
            command_0 = "sshpass -p'"+ user_pass + "' ssh " + user_name + "@" + machine.mac + " rm -r " + cluster_name 
            command_1 = "sshpass -p'"+ user_pass + "' ssh " + user_name + "@" + machine.mac + " mkdir " + cluster_name 
            command_2 = "sshpass -p'"+ user_pass + "' ssh " + user_name + "@" + machine.mac + " mkdir " + cluster_name+"/"+machine.node 
            dir_path = os.path.dirname(os.path.realpath(__file__))



            try:
                os.system(command_0)
            except:
                print("Error on command: ", command_0)
            try:
                os.system(command_1)
            except:
                print("Error on command: ", command_1)
            try:
                os.system(command_2)
            except:
                print("Error on command: ", command_2)
            #os.system(command_2)
            file_designation = "send_"+node_name+".py"
            output_file = open(file_designation, "w" )
            file_tag = "send_"+node_name+"_"+str(numerical_designation)
            write_string = "import os"+"\n"
            output_file.write(write_string)
            write_string = "import socket"+"\n"
            output_file.write(write_string)
            write_string = "# Custom file distribution protocal for"+file_tag+"\n"
            output_file.write(write_string)
            for destination_machine in cluster_members:
                if(destination_machine != machine):
                    write_string = 'os.system("'+ "sshpass -p '" + user_pass +"' scp -r /home/"+user_name+"/"+cluster_name+"/"+machine.node +"  "+ user_name +"@"+destination_machine.mac+":/home/"+user_name+"/"+cluster_name +'")\n'
                    output_file.write(write_string)

            
            write_string = "print('" + machine.mac + "')"+ "\n"
            output_file.write(write_string)
            write_string = "print('" + machine.node + "')"+ "\n"
            output_file.write(write_string)
            output_file.close()
            command_3 = "sshpass -p'"+ user_pass + "' scp "+dir_path+"/"+file_designation+" " + user_name + "@" + machine.mac +":/home/"+user_name+"/"+cluster_name
            try:
                os.system(command_3)
            except:
                print("Error on command: ", command_3)

            command_4 = "sshpass -p'"+ user_pass + "' scp "+dir_path+"/distributed_ledger_functions.py"+" " + user_name + "@" + machine.mac +":/home/"+user_name+"/"+cluster_name
            try:
                os.system(command_4)
            except:
                print("Error on command: ", command_4)

            command_4 = "sshpass -p'"+ user_pass + "' scp "+dir_path+"/cpu_temptest.py"+" " + user_name + "@" + machine.mac +":/home/"+user_name+"/"+cluster_name
            try:
                os.system(command_4)
            except:
                print("Error on command: ", command_4)

            command_5 = "sshpass -p'"+ user_pass + "' scp "+dir_path+"/distributed_ledger.bin"+" " + user_name + "@" + machine.mac +":/home/"+user_name+"/"+cluster_name
            try:
                os.system(command_5)
            except:
                print("Error on command: ", command_6)
            command_6 = "sshpass -p'"+ user_pass + "' scp "+dir_path+"/run_node.py"+" " + user_name + "@" + machine.mac +":/home/"+user_name+"/"+cluster_name
            try:
                os.system(command_6)
            except:
                print("Error on command: ", command_6)
            command_6 = "sshpass -p'"+ user_pass + "' scp "+dir_path+"/info.txt"+" " + user_name + "@" + machine.mac +":/home/"+user_name+"/"+cluster_name
            try:
                os.system(command_6)
            except:
                print("Error on command: ", command_6)
            command_6 = "sshpass -p'"+ user_pass + "' scp "+dir_path+"/nodes.txt"+" " + user_name + "@" + machine.mac +":/home/"+user_name+"/"+cluster_name
            try:
                os.system(command_6)
            except:
                print("Error on command: ", command_6)
            try:
                print("cleaning...",file_designation )
                os.system("rm "+ file_designation)
            except:
                print("Error on cleaning up files")
            numerical_designation = numerical_designation + 1

        


    #print(Nodes)
    #Nodes = unique(Nodes)
    #print(Nodes)
    #inets = unique(inets)

def activate_cluster():
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
    os.system("ls")
    file = open("info.txt", "r")
    for line in file:
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
    file.close()
    in_file = open("nodes.txt", "r") 
    for line in in_file:
        if(line[0] == "m"):
            new_inet = line[1:].rstrip(' \n')
            inets.append(new_inet)
    in_file.close()
    for mac in inets:
        command_1 = "sshpass -p'"+ user_pass + "' ssh " + user_name + "@" + mac + " ls "+  "/home/"+user_name+"/"+cluster_name+"/"
        command_2 = "sshpass -p'"+ user_pass + "' ssh " + user_name + "@" + mac + " cd "  "/home/"+user_name+"/"+cluster_name+ "/ && python3.7 run_node.py"

        try:
            os.system(command_1)
        
            print(".!.!.!.!.!.!. NODE "+ mac  + " ONLINE .!.!.!.!.!.!.")
            time.sleep(3)
        except:
            print("Error on command: ", command_1)
        try:
            os.system(command_2)
        
            print(".!.!.!.!.!.!. NODE "+ mac  + " ONLINE .!.!.!.!.!.!.")
            time.sleep(3)
        except:
            print("Error on command: ", command_2)



build_cluster()
activate_cluster()











