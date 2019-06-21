import os
import socket
# Custom file distribution protocal for send_Unit00_2
dir_path = os.path.dirname(os.path.realpath(__file__)) 
os.chdir(dir_path) 
os.system("sshpass -p 'ass_word' scp -r /home/tabasco_slim/Good_boi/Machine02  tabasco_slim@192.168.1.00:/home/tabasco_slim/Good_boi")
os.system("sshpass -p 'ass_word' scp -r /home/tabasco_slim/Good_boi/Machine02  tabasco_slim@192.168.1.01:/home/tabasco_slim/Good_boi")
os.system("sshpass -p 'ass_word' scp -r /home/tabasco_slim/Good_boi/Machine02  tabasco_slim@192.168.1.03:/home/tabasco_slim/Good_boi")
print('192.168.1.02')
print('Machine02')
