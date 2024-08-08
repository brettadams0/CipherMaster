def caesar_encrypt(plaintext, shift):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            encrypted += chr(start + (ord(char) - start + shift_amount) % 26)
        else:
            encrypted += char
    return encrypted
