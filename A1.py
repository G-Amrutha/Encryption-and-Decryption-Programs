import random as rd
import socket


def generate_OTP_key():
    # Q1.1
    # Generate List using random library
    key = "".join(map(str, rd.choices([0, 1], k=1000)))
    with open("OTPGeneratedKey.dat", "w") as ogk:
        ogk.write(key)


def convert_text_to_binary():
    # Q1.2
    # Read the given data-file
    with open("Letter.dat", "r") as f_text:
        text = f_text.read()
        
    # Convert text to binary
    res = ''.join(format(ord(i), 'b') for i in text)
    print(len(res), res)
    
    # Write binary string
    with open("LetterBinary.dat", "w") as f_bin:
        f_bin.write(res)


def crypt(string, key):
    # Auxiliary function for Q1.3
    # Crypts binary message with binary key by XOR
    k = int(key)
    msg = int(string)
    return str(k^msg)


def OTP_encrypt():
    # Q1.3
    # Read key file
    with open("OTPGeneratedKey.dat", "r") as ogk:
        key = ogk.read()
    
    # Read message file
    with open("LetterBinary.dat", "r") as lb:
        msg = lb.read()
        
    # Encrypt
    encrypted = crypt(msg, key)
    
    # Write encrypted message
    with open("protocoloneoutput.dat", "w") as poo:
        poo.write(encrypted)


def transmit_message():
    # Q1.4
    # Read protocoloneoutput.dat
    with open("protocoloneoutput.dat", "r") as poo:
        encrypted = poo.read()
    
    # Reserve a port for your service.
    port = 15734 
    
    # Create a socket object
    conn = socket.socket() 
    
    # Replace string with Bob's hostname
    conn.connect(("DESKTOP-79R0P34", port)) 
    
    # Transmit message
    conn.sendall(bytes(encrypted, 'utf-8'))
    print("File sent")
    
    # Close the socket when done
    conn.close() 
        
    
if __name__ == "__main__":
    generate_OTP_key() # key is generated
    convert_text_to_binary() # letter is made binary
    OTP_encrypt() # letter is OTP encrypted
    transmit_message() # encrypted letter is sent
        
        
        
        