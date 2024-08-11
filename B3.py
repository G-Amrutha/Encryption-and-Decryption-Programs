import socket
import hashlib

def receive():
    # Reserve a port for your service.
    port = 15500 
    
    # Create a socket object
    conn = socket.socket() 
    
    # Replace string with Alice's computer name
    conn.connect(('DESKTOP-RL35NF5', port))
    
    msg = [None, None]
    for i in range(2):
        while True:
            m = conn.recv(1024)
            msg[i] = m
            if m:
                while m:
                    m = conn.recv(1024)
                    msg[i] += m
                else:
                    break
    print("Done receiving")
    return msg

def crypt(string, key):
    # Auxiliary function for Q1.3
    # Crypts binary message with binary key by XOR
    k = int(key)
    msg = int(string)
    return str(k^msg)


def OTP_decrypt():
    # Q1.3
    # Read key file
    with open("OTPGeneratedKey.dat", "r") as ogk:
        key = ogk.read()
    
    # Read encrypted message
    with open("protocoloneoutput.dat", "r") as poo:
        msg = poo.read()
    
    # Encrypt
    decrypted = crypt(msg, key)
    
    # Write message file
    with open("LetterBinary.dat", "w") as lb:
        lb.write(decrypted)
    
    return decrypted
        
def convert_binary(string):
    text = ""
    for i in range(0, len(string), 7):
        text += chr(int(string[i:i+7], 2))
    return text
   
if __name__ == "__main__":
    # Receive from Alice
    data, hashcode = receive()
    
    # Find sha256 of file data
    m = hashlib.sha256()
    m.update(bytes(data, "utf-8"))
    Bob_code = m.digest()
    
    # Check Hashcode
    try:
        assert hashcode == Bob_code
        print("Message received okay")
        with open("protocoloneoutput.dat", "w") as f:
            f.write(data)
        enc = OTP_decrypt()
        OTP = convert_binary(enc)
        print(OTP)
    except:
        print("Error in Message")
    
    
    
    
