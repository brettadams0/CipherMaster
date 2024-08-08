def custom_decrypt(ciphertext, key):
    decrypted = ""
    for i, char in enumerate(ciphertext):
        shift = ord(key[i % len(key)]) % 26
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decrypted += chr(start + (ord(char) - start - shift + 26) % 26)
        else:
            decrypted += char
    return decrypted
