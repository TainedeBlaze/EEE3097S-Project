from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP 
import binascii

global keyPair 
global pubKey 
#pair used for the encryption 
keyPair = RSA.generate(5012)
pubKey = keyPair.publickey() 


#print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))
 
#print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))
 
#encryption
msg = 'A message for encryption'
encryptor = PKCS1_OAEP.new(pubKey)





#Allows someone to enter filename for encryption 
def encrypt(filename , key ):
    #reads in data and encrypts it 
    with open(filename , "rb") as file_out:
         filedata = file_out.read 
    global encrypted_data
    encrypted_data= RSA.encrypt(filedata,pubKey)  
    #encrypted_data= RSA.RsaKey.encrypt(filedata.encode() , pubKey)
#creates empty file and appends encrypted data to it 
    with  open("encryptedTxt.txt", "wb") as fp:
         fp.write(encrypted_data )
    fp.close() 

def decrypt(filename , key ): 
    ciphertext = open(filename , "rb")
    cipherdata = ciphertext.read() 
    global decrypted_data 
    decrypted_data = RSA.decrypt(cipherdata )




if __name__ == '__main__' : 
    fileIn = input() 
    encrypt(fileIn, pubKey) 
    print(encrypted_data)
