from Crypto.PublicKey import RSA 
from cryptography.fernet import Fernet
import time

def createkeys(): 
    start_time = time.time()
    #creating symetric key first 
    key = Fernet.generate_key() 
    #print(key.decode())

    #we now write that key to a file 
    k = open("symetricKey.key" , "wb" )
    k.write(key) 
    k.close() 

    #Creatng rsa public and private keys
    keyPair= RSA.generate(1024)
    pubKey = keyPair.publickey() 

    #writing public key to file 
    p = open("Publickey.key" , "wb")
    pubKeyPEM = pubKey.exportKey()
    p.write(pubKeyPEM)
    p.close() 

    #writing private key in file 
    pr = open("Privatekey.Key", "wb")
    privKeyPEM = keyPair.exportKey() 
    pr.write(privKeyPEM)
    pr.close() 
    print("The time to create keys took: ")
    print("--- %s seconds ---" % (time.time() - start_time))