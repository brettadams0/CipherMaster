def vigenere_encrypt(plaintext, key):
    encrypted = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('A')
            start = ord('A') if char.isupper() else ord('a')
            encrypted += chr(start + (ord(char) - start + shift) % 26)
            key_index += 1
        else:
            encrypted += char

    return encrypted
