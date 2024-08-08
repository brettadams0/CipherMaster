from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64


def generate_key():
    return base64.b64encode(DES.get_random_bytes(8)).decode('utf-8')

def des_encrypt(plaintext, key):
    cipher = DES.new(base64.b64decode(key), DES.MODE_ECB)
    encrypted = cipher.encrypt(pad(plaintext.encode(), DES.block_size))
    return base64.b64encode(encrypted).decode('utf-8')
