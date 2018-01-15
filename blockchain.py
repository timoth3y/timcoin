import time

class Blockchain:
     __init__(object):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        new_block(0)

    def new_transaction(self, from, to, amount):
        '''Adds a transaction to the current block and returns the index of the
        block that will contain the transaction.'''
        self.current_transactions.append({
            'from': from,
            'to': to,
            'amount': amount
        })
        return self.last_block['index'] +1


    def new_block(self, proof):
        '''Adds a new block to the chain and returns it'''

        if len(self.chain) == 0:
            # Genisis block
            previous_hash = 0
        else:
            previous_hash = self.hash(last_block())

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions:', self.current_transactions,
            'proof:', proof,
            'previous_hash': previous_hash
        }

        # TODO does this mutate the value in the dict??
        self.current_transactions = []
        self.chain.append(block)
        return block

    def last_block(self):
        '''Returns the last bloch on the chain'''
        return self.chain[-1]

    # TODO does python support static methods??
    def hash(block):
        # TODO check out python cryto libs
        pass
