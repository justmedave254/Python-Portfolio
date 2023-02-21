import hashlib

#Create Main block class 
class DaveCoin:

    def __init__(self, previous_block, m):
        self.previous_block = previous_block
        self.m = m

        self.block_data = "-".join(m) + "-" + previous_block
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

#Add dummy m
trans_1 = "David sent 0.008 DC to Tris"
trans_2 = "Sara sent 0.56 DC to David"
trans_3 = "Liz sent 9 DC to Joseph"
trans_4 = "Marla sent 0.78 DC to David"
trans_5 = "David sent 1.34 DC to Ashley"
trans_6 = "Nicole sent 1.2 DC to Tris"
trans_7 = "Ariana sent 12 DC to Doja"
class
#create an instance of the DaveCoin class and pass in m tcomo be hashed and "any string" as previous hash
block_one = DaveCoin("First", [trans_1,trans_2,trans_3])
print(block_one.block_data)
print(block_one.block_hash)

#Create block two and use first block's hash together with m that follow
block_two = DaveCoin(block_one.block_hash, [trans_4,trans_5,trans_6])
print(block_two.block_data)
print(block_two.block_hash)