"""
time lib is to get real time 
hashlib is used to hash the given block
"""
import time
import hashlib

#creating a chain which will contain all the blocks
chain = []

#creating the first block and its hash than adding it to chain
block0 = {
    "index": 0,
    "timestamp": time.time(),
    "data": "Genesis Block",
    "previous_hash": "0",
}
block0["hash"] = hashlib.sha256(str(block0).encode()).hexdigest()
chain.append(block0)


#function to add block in recursion 
def add_block(chain,data):
    last_block = chain[-1]
    block = {
        "index": len(chain),
        "timestamp": time.time(),
        "data": data,
        "previous_hash": last_block["hash"]

    }
    block_string = str(block)
    block["hash"]= hashlib.sha256(block_string.encode()).hexdigest()

    # Append to chain
    chain.append(block)


#function which will validate the blocks
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
    return True

add_block(chain,"data1")
add_block(chain,"data2")
print(chain)
print(is_chain_valid(chain))


