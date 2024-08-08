from encryption import caesar, vigenere, substitution, aes, des, custom_cipher
from decryption import caesar as dec_caesar, vigenere as dec_vigenere, substitution as dec_substitution, aes as dec_aes, des as dec_des, custom_cipher as dec_custom_cipher
from brute_force import caesar as bf_caesar, vigenere as bf_vigenere
from analysis import frequency
from keys import key_manager

def show_menu():
    print("\nPlease choose an option:")
    print("1. Encrypt a Message")
    print("2. Decrypt a Message")
    print("3. Brute Force Decrypt (Classical Ciphers)")
    print("4. Frequency Analysis")
    print("5. Manage Keys (Save/Load Keys)")
    print("6. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        encrypt_menu()
    elif choice == "2":
        decrypt_menu()
    elif choice == "3":
        brute_force_menu()
    elif choice == "4":
        frequency_analysis()
    elif choice == "5":
        key_manager_menu()
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")

def encrypt_menu():
    print("\nChoose encryption method:")
    print("[1] Caesar")
    print("[2] Vigenère")
    print("[3] Substitution")
    print("[4] AES")
    print("[5] DES")
    print("[6] Custom Cipher")
    choice = input("Enter your choice: ")
    plaintext = input("Enter the plaintext: ")

    if choice == "1":
        shift = int(input("Enter the shift value: "))
        print(f"Encrypted Message: {caesar.caesar_encrypt(plaintext, shift)}")
    elif choice == "2":
        key = input("Enter the key: ")
        print(f"Encrypted Message: {vigenere.vigenere_encrypt(plaintext, key)}")
    elif choice == "3":
        key = substitution.generate_key()
        print(f"Encrypted Message: {substitution.substitution_encrypt(plaintext, key)}")
    elif choice == "4":
        key = aes.generate_key()
        print(f"Encrypted Message: {aes.aes_encrypt(plaintext, key)}")
    elif choice == "5":
        key = des.generate_key()
        print(f"Encrypted Message: {des.des_encrypt(plaintext, key)}")
    elif choice == "6":
        key = custom_cipher.generate_key()
        print(f"Encrypted Message: {custom_cipher.custom_encrypt(plaintext, key)}")
    else:
        print("Invalid choice. Please try again.")

def decrypt_menu():
    print("\nChoose decryption method:")
    print("[1] Caesar")
    print("[2] Vigenère")
    print("[3] Substitution")
    print("[4] AES")
    print("[5] DES")
    print("[6] Custom Cipher")
    choice = input("Enter your choice: ")
    ciphertext = input("Enter the ciphertext: ")

    if choice == "1":
        shift = int(input("Enter the shift value: "))
        print(f"Decrypted Message: {dec_caesar.caesar_decrypt(ciphertext, shift)}")
    elif choice == "2":
        key = input("Enter the key: ")
        print(f"Decrypted Message: {dec_vigenere.vigenere_decrypt(ciphertext, key)}")
    elif choice == "3":
        key = substitution.generate_key()
        print(f"Decrypted Message: {dec_substitution.substitution_decrypt(ciphertext, key)}")
    elif choice == "4":
        key = input("Enter the AES key: ")
        print(f"Decrypted Message: {dec_aes.aes_decrypt(ciphertext, key)}")
    elif choice == "5":
        key = input("Enter the DES key: ")
        print(f"Decrypted Message: {dec_des.des_decrypt(ciphertext, key)}")
    elif choice == "6":
        key = input("Enter the custom key: ")
        print(f"Decrypted Message: {dec_custom_cipher.custom_decrypt(ciphertext, key)}")
    else:
        print("Invalid choice. Please try again.")

def brute_force_menu():
    print("\nChoose brute force method:")
    print("[1] Caesar")
    print("[2] Vigenère")
    choice = input("Enter your choice: ")
    ciphertext = input("Enter the ciphertext: ")

    if choice == "1":
        bf_caesar.caesar_brute_force(ciphertext)
    elif choice == "2":
        bf_vigenere.vigenere_brute_force(ciphertext)
    else:
        print("Invalid choice. Please try again.")

def frequency_analysis():
    ciphertext = input("Enter the ciphertext for frequency analysis: ")
    analysis = frequency.frequency_analysis(ciphertext)
    print("Frequency Analysis:")
    for char, freq in analysis.items():
        print(f"{char}: {freq}")

def key_manager_menu():
    print("\nKey Management:")
    print("[1] Save Key")
    print("[2] Load Key")
    choice = input("Enter your choice: ")

    if choice == "1":
        key = input("Enter the key to save: ")
        filename = input("Enter the filename to save the key: ")
        key_manager.save_key(key, filename)
        print("Key saved successfully.")
    elif choice == "2":
        filename = input("Enter the filename to load the key: ")
        key = key_manager.load_key(filename)
        print(f"Loaded Key: {key}")
    else:
        print("Invalid choice. Please try again.")
