import itertools
from string import ascii_uppercase
from decryption import vigenere as dec_vigenere

def vigenere_brute_force(ciphertext):
    import itertools
    from string import ascii_uppercase

    for length in range(1, 6):  # Trying key lengths from 1 to 5
        for key in itertools.product(ascii_uppercase, repeat=length):
            key = ''.join(key)
            decrypted = dec_vigenere.vigenere_decrypt(ciphertext, key)
            print(f"Key '{key}': {decrypted}")
