#importing time so that we can get the current time
import time
#impoting hash-lib which will import hash fucntions in python
import hashlib

#creating the first block
block0 = {
    "index": 0,
    "timestamp": time.time(),
    "data": "Genesis Block",
    "previous_hash": "0",
}
#creating whole genesis block to string so that we can hash the string 
block0_string = str(block0)
#hashing the string and stroring the hash in the block
block0["hash"] = hashlib.sha256(block0_string.encode()).hexdigest()

#creating block 1 which previous hash of hash genesis block 
block1 = {
    "index": 1,
    "timestamp": time.time(),
    "data": "block 1",
    "previous_hash": block0["hash"]
}
#creating string of block 2
block1_string = str(block1)
#hashing the string and stroring the hash in the block
block1["hash"] = hashlib.sha256(block1_string.encode()).hexdigest()

#creating a function which will validate the blocks
def is_chain_valid(chain):
    for i in range(1,len(chain)):
        current_block = chain[i]
        previous_block = chain[i-1]

        #recalculate the hash of current block but firstly we have to pop the hash of current block 
        copy_of_current_block = current_block.copy()
        copy_of_current_block.pop("hash")
        recalculated_hash = hashlib.sha256((str(copy_of_current_block)).encode()).hexdigest()

        if recalculated_hash != current_block["hash"]:
            print("chain have been tampered with") 
            return False
        if current_block["previous_hash"] != previous_block["hash"]:
            print("you have wrong hash")
            return False
    print("yay")
    return True

chain = [block0,block1]
is_chain_valid(chain)
