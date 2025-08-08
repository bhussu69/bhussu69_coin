"""
time    -> to get real time
hashlib -> to hash the given block
json    -> because str(dict) can mess up key order and break hashing
"""
import time
import hashlib
import json

# Blockchain parameters
DIFFICULTY = 5  # required number of leading zeros in the hash


# helper: compute hash for a block (excluding its own 'hash' field)
def compute_hash(block):
    temp = block.copy()
    temp.pop("hash", None)
    block_string = json.dumps(temp, sort_keys=True)
    return hashlib.sha256(block_string.encode()).hexdigest()


# function to add a block
def add_block(chain, data):
    last_block = chain[-1]
    block = {
        "index": len(chain),
        "timestamp": time.time(),
        "data": data,
        "previous_hash": last_block["hash"],
        "nonce": 0
    }

    while True:
        block["hash"] = compute_hash(block)
        if block["hash"].startswith("0" * DIFFICULTY):
            break
        block["nonce"] += 1

    chain.append(block)


# function to validate the blockchain
def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current_block = chain[i]
        previous_block = chain[i - 1]

        # check hash validity
        if compute_hash(current_block) != current_block["hash"]:
            print(f"Block {i} has been tampered with")
            return False

        # check previous hash linkage
        if current_block["previous_hash"] != previous_block["hash"]:
            print(f"Block {i} has wrong previous_hash")
            return False

    return True


# create chain list
chain = []

# create genesis block
genesis_block = {
    "index": 0,
    "timestamp": time.time(),
    "data": "Genesis Block",
    "previous_hash": "0",
    "nonce": 0
}

while True:
    genesis_block["hash"] = compute_hash(genesis_block)
    if genesis_block["hash"].startswith("0" * DIFFICULTY):
        break
    genesis_block["nonce"] += 1

chain.append(genesis_block)

# add more blocks
add_block(chain, "data1")
add_block(chain, "data2")

# print results
print(chain)
print(is_chain_valid(chain))
