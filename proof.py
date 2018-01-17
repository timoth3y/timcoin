import hashlib

def proof_of_work(previous_block_hash):
    proof = 0
    while not validate_proof_of_work(proof, previous_block_hash):
        proof += 1

    return proof


def validate_proof_of_work(proof, previous_block_hash):

    hash_stub = previous_block_hash[-20:]
    challenge_bytes = f"{previous_block_hash}{proof}".encode('utf-8')
    hash_val = hashlib.sha256(challenge_bytes).hexdigest()
    return hash_val[:4] == '0000'
