# Encryption and Decryption Programs

This project consists of Python scripts that demonstrate encryption and decryption techniques using one-time pad (OTP), Diffie-Hellman key exchange, and AES encryption.

## Files

- `A1.py`: Generates a one-time pad key, converts text to binary, and encrypts the binary text using the generated key.
- `A2.py`: Implements Diffie-Hellman key exchange and message encryption using a one-time pad.
- `A3.py`: Generates a one-time pad key and converts text to binary for encryption.
- `B1.py`: Receives and decrypts a file using a one-time pad.
- `B2.py`: Implements Diffie-Hellman key exchange and uses AES encryption for secure communication.
- `B3.py`: Receives encrypted messages and decrypts them using a one-time pad.

## Requirements

- Python 3.x
- `pycryptodome` library for AES encryption

## Usage

### A1.py

1. **Generate OTP Key**:
   - The script automatically generates a 1000-bit OTP key and saves it to `OTPGeneratedKey.dat`.

2. **Convert Text to Binary**:
   - Ensure `Letter.dat` contains the text you want to encrypt.
   - Run the script to convert this text to binary, which will be saved in `LetterBinary.dat`.

3. **Encrypt Binary Text**:
   - The script will use the generated OTP key to encrypt the binary text, with results stored in a specified file.

### A2.py

1. Calculate public and secret keys using Diffie-Hellman.
2. Encrypt a message using a one-time pad and send it over a socket connection.

### A3.py

1. Generate a 1000-bit OTP key.
2. Convert text from `Letter.dat` to binary.
3. Encrypt the binary text using the OTP key.

### B1.py

1. Connect to a remote server to receive an encrypted file.
2. Decrypt the received file using a one-time pad.

### B2.py

1. Calculate public and secret keys using Diffie-Hellman.
2. Use AES encryption for secure message transmission.

### B3.py

1. Connect to a server to receive encrypted messages.
2. Decrypt the messages using a one-time pad.

## Running the Scripts

Run each script using:

```bash
python script_name.py
```

Ensure that any required input files (e.g., `Letter.dat`) are in the same directory as the scripts or update the file paths accordingly.
