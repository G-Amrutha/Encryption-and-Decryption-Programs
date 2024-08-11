import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import socket


# Information known to Alice
p, g = 7, 5   #Diffie Hellman Modulus and Base
alice_private = 4 #private key
bob_public = 6    #public key
bob_comp = "DESKTOP-79R0P34"


def find_public():
    # Diffie Hellman Formula 1
    return pow(g, alice_private, p)

def find_secret():
    # Diffie Hellman Formula 2
    return str(pow(bob_public, alice_private, p))

def read_OTP_key():
    # Read the OTP key
    with open("OTPGeneratedKey.dat", "r") as ogk:
        key = ogk.read()
    return key

def transmit_message(enc):
    # Q1.4
    # Reserve a port for your service.
    port = 15530
    
    # Create a socket object
    conn = socket.socket() 
    
    # Replace string with Bob's hostname
    # Can be obtained as socket.gethostname()
    # on Bob's Computer
    conn.connect((bob_comp, port)) 
    
    # Transmit message
    conn.sendall(bytes(enc, 'utf-8'))
    print("File sent")
    
    # Close the socket when done
    conn.close() 

class AESCipher(object):
    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


if __name__ == "__main__":
    aes = AESCipher(find_secret())
    cipher = aes.encrypt(read_OTP_key())
    transmit_message(cipher)
    print("Message sent AES encrypted with secret key")
