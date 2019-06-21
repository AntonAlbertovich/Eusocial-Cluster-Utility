import os
import socket
# Custom file distribution protocal for send_Node_2
dir_path = os.path.dirname(os.path.realpath(__file__)) 
os.chdir(dir_path) 
os.system("sshpass -p 'root' scp -r /home/user/Eusocial-Cluster/Machine02  user@192.168.1.00:/home/user/Eusocial-Cluster")
os.system("sshpass -p 'root' scp -r /home/user/Eusocial-Cluster/Machine02  user@192.168.1.01:/home/user/Eusocial-Cluster")
print('192.168.1.02')
print('Machine02')
