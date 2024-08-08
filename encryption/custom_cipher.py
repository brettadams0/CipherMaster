import random
import string

def generate_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def custom_encrypt(plaintext, key):
    encrypted = ""
    for i, char in enumerate(plaintext):
        shift = ord(key[i % len(key)]) % 26
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted += chr(start + (ord(char) - start + shift) % 26)
        else:
            encrypted += char
    return encrypted
