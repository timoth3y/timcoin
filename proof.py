import hashlib

def proof_of_work(last_proof):
    proof = 0
    while not validate_proof_of_work(proof, last_proof)
        proof += 1

    return proof


def validate_proof_of_work(proof, last_proof):

    challenge_str = "{}{}".format(last_proof, proof)
    hash_val = hashlib.sha256(challenge_str).hexdigest()

    pass
