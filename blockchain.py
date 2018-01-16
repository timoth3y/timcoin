import time
import hashlib

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(0)

    def new_transaction(self, sender, receiver, amount):
        '''Adds a transaction to the current block and returns the index of the
        block that will contain the transaction.'''
        self.current_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })

        #TODO maybe don't send retirn value
        return self.last_block()['index'] + 1


    def new_block(self, proof):
        '''Adds a new block to the chain and returns it'''

        if len(self.chain) == 0:
            # Genisis block
            self.previous_hash = 0
        else:
            self.previous_hash = self.hash(self.last_block())

        #TODO time() is only time compent. Need some kind of datetime
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': self.previous_hash
        }

        self.current_transactions = []
        self.chain.append(block)
        return block

    def last_block(self):
        '''Returns the last bloch on the chain'''
        return self.chain[-1]


    # TODO does python support static methods??
    def hash(self, block):
        # Can't hash objects or unicode strings
        # TODO This is a very fucked up hash fundtion
        # Need something more robest. Can't trust cascading implemetntations of __repr__
        strz = repr(block).encode('utf-8')
        hash_val = hashlib.sha256(strz).hexdigest()
        return hash_val
