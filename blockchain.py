import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce, self.hash = self.mine_block()

    def compute_hash(self, nonce):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty=4):
        nonce = 0
        computed_hash = self.compute_hash(nonce)
        while not computed_hash.startswith("0" * difficulty):
            nonce += 1
            computed_hash = self.compute_hash(nonce)
        return nonce, computed_hash

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_last_block()
        new_block = Block(len(self.chain), data, previous_block.hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.compute_hash(current.nonce):
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

    def print_chain(self):
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print(f"Prev Hash: {block.previous_hash}")
            print(f"Nonce: {block.nonce}")
            print("------")

if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_block("Transaksi 1: A -> B")
    blockchain.add_block("Transaksi 2: B -> C")
    blockchain.print_chain()
    print("Valid?", blockchain.is_valid())
