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

print(block0)
print(block1)
