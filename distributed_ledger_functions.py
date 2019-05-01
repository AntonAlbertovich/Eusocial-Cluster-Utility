import hashlib as hasher
import datetime as date
import pickle

class Block:
    #written by Anton Rakos
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        #written by Anton Rakos
        #This is the data structure which is often refured to as the block. It contains information such as the time when the 
        #block is created, the hash of the previous block in the chain, the hash of the current block and data relevent to a 
        #survey time for the local node within the cluster. 

        sha = ""
        sha.encode('utf-8')
        sha = hasher.sha256()
        sha.update(str(self.timestamp).encode('utf-8')+
                   str(self.data).encode('utf-8')+
                   str(self.previous_hash).encode('utf-8'))

        return sha.hexdigest()

def create_genesis_block():
    #By Anton Rakos
    #builds the first block in a blockchain
    output_file = open("distributed_ledger.bin", "wb")
    genesis_block = Block(date.datetime.now(), "Genesis Block", "0")
    blockchain = [genesis_block]
    pickle.dump(blockchain, output_file)
    output_file.close()

def next_block(this_input):
    #by Anton Rakos
    #generates the next block
    this_timestamp = date.datetime.now()
    this_data = str(this_input)
    input_file = open("distributed_ledger.bin", "rb")
    distributed_public_ledger = pickle.load(input_file)
    last_block =  distributed_public_ledger[len(distributed_public_ledger) - 1]
    this_hash = last_block.hash
    new_block = Block(this_timestamp, this_data, this_hash)
    input_file.close()
    output_file = open("distributed_ledger.bin", "wb")
    distributed_public_ledger.append(new_block)
    pickle.dump(distributed_public_ledger, output_file)
    output_file.close()

def view_distributed_public_ledger():
    #By Anton Rakos
    #prints the local distributed_ledger.bin file.
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

def verify_distributed_public_ledger():
    #by Anton Rakos
    #verifies that all the blocks in a block chain contain the correct previous hash
    # this ensure that the blocks were not tampered with.
    input_file = open("distributed_ledger.bin", "rb")
    distributed_public_ledger = pickle.load(input_file)
    verified = True
    for i in range(1, len(distributed_public_ledger)):
        this_block = distributed_public_ledger[i - 1]
        next_block = distributed_public_ledger[i]
        if(next_block.previous_hash != this_block.hash):
            verified = False
            break
    if(verified == True):
        print("distributed_ledger.bin has been verified.")
        return True
    else:
        return False
    
    input_file.close()
    


