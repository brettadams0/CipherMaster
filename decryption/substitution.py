from encryption.substitution import substitution_encrypt, generate_key
import string

def substitution_decrypt(ciphertext, key):
    """Decrypt ciphertext using a substitution cipher with the given key."""
    alphabet = string.ascii_uppercase
    key_map = str.maketrans(key, alphabet)
    ciphertext = ciphertext.upper()
    return ciphertext.translate(key_map)
