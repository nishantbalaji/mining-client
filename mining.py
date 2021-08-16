from hashlib import sha256
import time

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    solution = False
    nonce = 0
    while not solution: 
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print("Yay! Successfully mined with nonce:", nonce)
            solution = True
            return new_hash

        if not solution:
            nonce += 1

if __name__ == "__main__":
    transactions ='''
    Tom->Jerry->20,
    Mando->Cara->45
    '''
    difficulty = 4
    start = time.time()
    print("start mining")
    new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    total_time = str((time.time() - start))
    print("total time:", total_time)
    print(new_hash)