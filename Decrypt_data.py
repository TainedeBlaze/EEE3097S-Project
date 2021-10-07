from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA  
from Crypto.Cipher import PKCS1_OAEP
import time 
import sys

def decrypt(text): 
    start_time = time.time()
    # load the private key to decrypt 
    prkey = open("Privatekey.key" , "rb")
    pkey = prkey.read() 
    private_key= RSA.import_key(pkey)

    #open the encrypted public key 
    e = open("encryptedkey" , "rb")
    encrypted_key= e.read() 

    #decrypt the encrypted public key using the private key 
    decryptor = PKCS1_OAEP.new(private_key)
    decrypted = decryptor.decrypt(encrypted_key)

    #CREATE THE CIPHER USED FOR DECRYPTION  
    cipher = Fernet(decrypted)

    encrypted_data = open("encrypted_fileof"+str(text), "rb") 
    edata= encrypted_data.read() 

    decrypted_data = cipher.decrypt(edata)

    ##print(decrypted_data.decode())

    #write that to a new file 
    ThankGodIamDone = open( "decrypted_data.txt" ,  "wb" )
    ThankGodIamDone.truncate(0)
    ThankGodIamDone.write(decrypted_data)
    print("Decryption took: ")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':

    inputfile = sys.argv[1]
    decrypt(inputfile)