# CipherMaster

CipherMaster is a comprehensive terminal-based cryptography toolkit that supports multiple encryption and decryption algorithms. This project includes implementations of classical ciphers like Caesar and Vigenère, as well as modern encryption techniques such as AES and DES. It also features tools for brute-force decryption and cryptographic analysis.

## Features

- **Encryption Algorithms**:
  - Caesar Cipher
  - Vigenère Cipher
  - Substitution Cipher
  - AES (Advanced Encryption Standard)
  - DES (Data Encryption Standard)
  - Custom Cipher

- **Decryption Algorithms**:
  - Caesar Cipher
  - Vigenère Cipher
  - Substitution Cipher
  - AES
  - DES
  - Custom Cipher

- **Brute Force**:
  - Caesar Cipher Brute Force
  - Vigenère Cipher Brute Force

- **Analysis**:
  - Frequency Analysis for cryptographic analysis

- **Key Management**:
  - Save and load encryption keys

## Installation

1. Clone the repository:
```bash
git clone https://github.com/brettadams0/CipherMaster.git
```
Navigate to the project directory:

```bash
cd CipherMaster
```
Ensure you have Python 3 installed. Install necessary dependencies (if any).

## Usage
Run the program from the terminal:

```bash
python main.py
```
You will be presented with a menu to choose between solving a cipher or generating a new one. Follow the prompts to select the desired encryption or decryption method.

```bash
CipherMaster/
│
├── main.py                 # Entry point for the program
├── menu.py                 # Handles the main menu and user input
│
├── encryption/             # Contains implementations for encryption algorithms
│   ├── caesar.py           # Caesar Cipher encryption
│   ├── vigenere.py         # Vigenère Cipher encryption
│   ├── substitution.py     # Substitution Cipher encryption
│   ├── aes.py              # AES encryption
│   ├── des.py              # DES encryption
│   ├── custom_cipher.py    # Custom Cipher encryption
│
├── decryption/             # Contains implementations for decryption algorithms
│   ├── caesar.py           # Caesar Cipher decryption
│   ├── vigenere.py         # Vigenère Cipher decryption
│   ├── substitution.py     # Substitution Cipher decryption
│   ├── aes.py              # AES decryption
│   ├── des.py              # DES decryption
│   ├── custom_cipher.py    # Custom Cipher decryption
│
├── brute_force/            # Contains brute-force decryption tools
│   ├── caesar.py           # Brute force decryption for Caesar Cipher
│   ├── vigenere.py         # Brute force decryption for Vigenère Cipher
│
├── analysis/               # Contains analysis tools
│   ├── frequency.py        # Frequency analysis module
│
└── keys/                   # Key management utilities
    ├── key_manager.py      # Save/load key management
```

## Contributing
If you would like to contribute to CipherMaster, please fork the repository and submit a pull request with your proposed changes. For major changes or feature requests, please open an issue to discuss your ideas first.
