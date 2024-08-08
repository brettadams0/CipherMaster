import string
import random

def generate_key():
    """Generate a random substitution key."""
    letters = list(string.ascii_uppercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    return ''.join(shuffled)

def substitution_encrypt(plaintext, key):
    """Encrypt plaintext using a substitution cipher with the given key."""
    alphabet = string.ascii_uppercase
    key_map = str.maketrans(alphabet, key)
    plaintext = plaintext.upper()
    return plaintext.translate(key_map)

def substitution_decrypt(ciphertext, key):
    """Decrypt ciphertext using a substitution cipher with the given key."""
    alphabet = string.ascii_uppercase
    key_map = str.maketrans(key, alphabet)
    ciphertext = ciphertext.upper()
    return ciphertext.translate(key_map)
