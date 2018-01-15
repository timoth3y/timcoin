import pytest
from blockchain import Blockchain

#@pytest.fixture
#def empty_blockchain():
#    return Blockchain()


def test_setup():
    blockchain = Blockchain()
    assert len(blockchain.chain) == 1
    assert len(blockchain.current_transactions) == 0

    block = blockchain.last_block()
    assert block['index'] == 1
    assert len(block['transactions']) == 0
