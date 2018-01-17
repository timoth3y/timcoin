import hashlib
import proof



def test_proof_of_work():
    last_hash = hashlib.sha256("FooBar".encode('utf-8')).hexdigest()
    assert proof.proof_of_work(last_hash) == 270743


def test_validate_proof_of_work():
    last_hash = hashlib.sha256("FooBar".encode('utf-8')).hexdigest()
    print(last_hash)

    assert not proof.validate_proof_of_work(5, last_hash)
    assert proof.validate_proof_of_work(270743, last_hash)
