from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def generate_key():
    return base64.b64encode(AES.get_random_bytes(16)).decode('utf-8')

def aes_encrypt(plaintext, key):
    cipher = AES.new(base64.b64decode(key), AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(encrypted).decode('utf-8')
