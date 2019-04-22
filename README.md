**Eusociality** is defined by Wikipedia as the highest level of organization of sociality, is defined by the following characteristics: cooperative brood care, overlapping generations within a colony of adults, and a division of labor into reproductive and non-reproductive groups. 

**Summary of the Project:**
Philosophically speaking, Eusocial Cluster Utility was developed in direct opposition to cloud based computing.
A homemade super computer is the ultimate tool for developers working in machine learning, natural language processing, system simulations, or social media mining who do not wish to compromise the security of their data and risk computational throttling by the owner of a cloud web service. However the configuration of a local network cluster computer is not necessarily a simple task, nor is optimizing a cluster or ensuring that the safety of the hardware and integrity of the data. Eusocial Cluster Utility is an ongoing project which seeks to develop a interface for creating and managing a Debian Beowulf cluster. By using a publicly distributed ledger (also known as a blockchain) to record hardware analytic such as CPU usage and waste heat production, Eusocial Cluster Utility seeks to provide a secure method for ensuring the integrity of data which may later be used to optimize a cluster. As the primary objective of Eusocial Cluster Utility is to provide developers with a distributed platform for performing computationally expensive tasks, Eusocial-Cluster-Utility-0.9.3 comes bundled with a natural language processing bench mark test which uses the spaCy GPU software library for CUDA 10.0 in conjunction with the MediaWiki API. Eusocial Cluster Utility was originally developed by students at Texas Tech University in 2019 and is an on going open source project.

This utility has been developed and proven to work on Ubuntu 18.04 and requires the following dependencies: 

**Python 3.7** – which may be installed via the commands:
```
sudo apt-get install python3.7-dev
sudo apt install python3.7-minimal
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
