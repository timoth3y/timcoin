import pytest
from blockchain import Blockchain


@pytest.fixture
def loaded_blockchain():
    blockchain = Blockchain()
    blockchain = Blockchain()
    assert blockchain.new_transaction('foo', 'bar', 10) == 2
    assert blockchain.new_transaction('a-foo', 'a-bar', 2) == 2
    return blockchain


def test_setup():
    blockchain = Blockchain()
    assert len(blockchain.chain) == 1
    assert len(blockchain.current_transactions) == 0


def test_last_block(loaded_blockchain):
    block = loaded_blockchain.last_block()
    assert block['index'] == 1
    assert len(block['transactions']) == 0


def test_new_transaction(loaded_blockchain):
    assert len(loaded_blockchain.current_transactions) == 2

    assert loaded_blockchain.current_transactions[0]['sender'] == 'foo'
    assert loaded_blockchain.current_transactions[0]['receiver'] == 'bar'
    assert loaded_blockchain.current_transactions[0]['amount'] == 10

    assert loaded_blockchain.current_transactions[1]['sender'] == 'a-foo'
    assert loaded_blockchain.current_transactions[1]['receiver'] == 'a-bar'
    assert loaded_blockchain.current_transactions[1]['amount'] == 2



def test_new_block(loaded_blockchain):
    block = loaded_blockchain.new_block("fooHash")
    assert block == loaded_blockchain.last_block()
    assert block['index'] == 2
    assert len(block['transactions']) == 2
    assert block['proof'] == "fooHash"
    assert block['previous_hash']
