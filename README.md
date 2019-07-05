**Eusociality** is defined as the highest level of organization of sociality, and describes the cooperative nature of a given community to perform tasks and conduct internal maintenance. When apply this term to super computing,  Eusociality means that a tasks are properly delegated and that all the machines are properly utilized. The scheduling of tasks in a cluster can become very complicated if all the machines are not directly connected to one another, if some machine are not capable of solving some tasks, or if some tasks require the prior completion of other tasks and the transfer of their results. 


**A possibly NP-Complete Problem**
Let *B* represent a Beowulf Cluster in where the set *M* of *m* many machines are interconnected with the set *A* of *a* many authorized ssh connections.  The network of *B* can be represented by a directed graph with *m* vertices and *a* edges such that *m* < *a* and *m* > 1. Let    *H* be a subset A0 .. Am  of *A* which represents a set of directed edges from M0 to all members of *M*.  

A tasks is an action which may be transferred from M_i member of *M* to another member M_j of *M* so long as there exist an edge from M_i to M_j. A task may only be completed at a member of *M* if said member meets the proper requirements to complete said task. All tasks begin at M0.  No tasks may be completed at M0. Each task will travel once along one member of *H* to a machine capable of completing said task.  

Some tasks *t*, which is may only be executed on *x*, may require files produced by the completion a task belonging to the set *T*. All member of *T* must be completed prior to the completion of *t*. If a member of *X* is not completed on mi then said member must be transferred to *x* prior to the completion of *t*. 

Given a configuration of some *B* with the requirements of all tasks corresponding with the capabilities of all members of *M*, can a plan for transferring and completing tasks be made? If so state said plan.

Eusocial Cluster Utility is capable of solving this problem via modeling the details of tasks and machines in Answer Sets. 

To View this Answer Set Programming feature of Eusocial Cluster Utility simply download the repository and open up the master directory and enter:
```
python3 main.py
```
Then select the button:

Build Schedule

The following files are associated with the Answer Set Programming portion of ECU:

configuring_menu.py

All file in the GUI_functions directory. 

**Summary of the Project:**
Eusocial Cluster Utility is being developed for the users who want to distribute tasks across a Beowulf Cluster. Eusocial Cluster Utility, or ECU for short, assumes all machines in a user’s cluser are using either Debian or Red Hats Linux.  ECU was originally developed and tested on CentOS 7 and Ubuntu 18.04.  By using a publicly distributed ledger (also known as a blockchain) to record hardware analytic such as CPU usage and waste heat production, Eusocial Cluster Utility seeks to provide a secure method for ensuring the integrity of data which may later be used to optimize a cluster. As the primary objective of Eusocial Cluster Utility is to provide developers with a distributed platform for performing computationally expensive tasks, Eusocial-Cluster-Utility-0.9.3 comes bundled with a natural language processing bench mark test which uses the spaCy GPU software library for CUDA 10.0 in conjunction with the MediaWiki API. Eusocial Cluster Utility was originally developed by students at Texas Tech University in 2019 and is an on going open source project.

This utility has been developed and proven to work on Ubuntu 18.04 and requires the following dependencies: 

**Python 3.7** – which may be installed via the commands:
```
sudo apt-get install python3.7-dev
sudo apt install python3.7-minimal
```

**Clingo** – which may be installed via the commands:
```
conda install -c potassco clingo 
conda install -c potassco/label/dev clingo
pip install clyngor-with-clingo
```
**psutil** – which may be installed specifically for python3.7 via the command:
```
python3.7 -m pip install psutil
```
**tkinter** – which does not come standard for python3 on Ubuntu 18.04 and may be installed via the command:
```
sudo apt-get install python-tk python3-tk tk-dev
```
To run simply download Eusocial-Cluster-Utility, extract the master directory, navigate into Eusocial-Cluster-Utility-master, and run the command:
```
python3 main.py
```
Eusocial-Cluster-Utility includes a graphic uster interface which will guide you through the creation of your cluster. 

**OpenSSH server** -- which may be install via the commands:
```
sudo apt-get -y install gfortran
sudo apt-get -y install openssh-server
```
**sshpass** -- which may be installed via the command:
```
sudo apt-get -y install sshpass
```

**Eusocial-Cluster-Utility** -- To begin the installation process for the utility and open the graphic user interface run the following commands:
```
wget https://github.com/AntonAlbertovich/Eusocial-Cluster-Utility/archive/v0.9.3.zip
unzip v0.9.3.zip
cd Eusocial-Cluster-Utility-0.9.3/
python3.7 main.py
```

OPTIONAN: For NLP test bench only
If you would like to run the NLP test bench and have an Nvidia GPU then the following commands to install the appropritate drivers will be nessary. If you already have Cuda 10.0 installed and set as your primary NVCC tool kit then you may skip ahead to the next set of commands:
```
sudo apt-get purge nvidia*
sudo add-apt-repository ppa:graphics-drivers
sudo apt-get update
sudo apt-get -u install nvidia-390
sudo reboot
cd Downloads/
wget https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda-repo-ubuntu1804-10-0-local-10.0.130-410.48_1.0-1_amd64
sudo dpkg -i cuda-repo-ubuntu1804-10-0-local-10.0.130-410.48_1.0-1_amd64
sudo apt-key add /var/cuda-repo-10-0-local-10.0.130-410.48/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda-10-0
```
Add the following lines to your .bashrc file:

       export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}
       export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}
```
sudo apt-get update
reboot
```
**MediaWiki python wikipedia api** and **spaCy with GPU** may be installed with the following commands:
```
pip3 install wikipedia
pip3 install -U spacy
python3 -m spacy download en
pip3 install cupy-cuda100
pip3 install -U spacy[cuda100]
```
