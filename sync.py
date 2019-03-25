import os
import socket

#This is an example of the command used to send files from one machine to another

#In this example the machine recieving the files is machine Unit01 and the machine sending the files is Unit00

#In this example the dircetory being sent is named Unit00 after the machine from which it is being sent. 

#In this example the name Unit01 has already been configured in the hosts directory, allowing an ssh into via the command: ssh Unit01 

os.system("sshpass -p '!YOUR SSH PASSWORD!' scp -r /home/USER_NAME/Eusocial_Cluster/Unit00 Unit01:/home/tabasco-slim/Eusocial_Cluster")
print("Sync with Unit01 complete")

