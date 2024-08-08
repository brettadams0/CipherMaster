def vigenere_decrypt(ciphertext, key):
    decrypted = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('A')
            start = ord('A') if char.isupper() else ord('a')
            decrypted += chr(start + (ord(char) - start - shift + 26) % 26)
            key_index += 1
        else:
            decrypted += char

    return decrypted
