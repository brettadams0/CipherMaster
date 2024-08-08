from decryption import caesar as dec_caesar

def caesar_brute_force(ciphertext):
    for shift in range(26):
        decrypted = dec_caesar.caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted}")
