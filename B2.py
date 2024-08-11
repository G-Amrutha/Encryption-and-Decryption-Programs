import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import socket


p, g = 7, 5
bob_private = 51
alice_public = 2


def find_public():
    return pow(g, bob_private, p)


def find_secret():
    return str(pow(alice_public, bob_private, p))


def receive_file():
    # Reserve a port for your service.
    port = 16800 
    
    # Create a socket object
    conn = socket.socket() 
    
    # Replace string with Alice's computer name
    conn.connect(('DESKTOP-RL35NF5', port))
    
    data = None
    while True:
        m = conn.recv(1024)
        data = m
        if m:
            while m:
                m = conn.recv(1024)
                data += m
            else:
                break

    print("Done receiving")
    return data


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
    cipher = receive_file()
    aes = AESCipher(find_secret())
    OTP_key = aes.decrypt(cipher)
    with open("OTP_key.dat", "w") as f:
        f.write(OTP_key)
