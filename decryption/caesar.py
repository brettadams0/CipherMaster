def caesar_decrypt(ciphertext, shift):
    """Decrypt a message encrypted with the Caesar cipher using the given shift."""
    decrypted_message = []

    # Iterate through each character in the ciphertext
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            # Determine the base (upper or lower case)
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet if needed
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_message.append(decrypted_char)
        else:
            # Non-alphabetic characters are added unchanged
            decrypted_message.append(char)

    return ''.join(decrypted_message)
