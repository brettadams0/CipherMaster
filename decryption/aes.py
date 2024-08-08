from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64


def aes_decrypt(ciphertext, key):
    cipher = AES.new(base64.b64decode(key), AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(base64.b64decode(ciphertext)), AES.block_size)
    return decrypted.decode('utf-8')
