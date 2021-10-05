from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA  
from Crypto.Cipher import PKCS1_OAEP
import time 


def encrypt():
    start_time = time.time()
    #open the symetric key file 
    skey = open("symetricKey.key" , "rb" )
    key = skey.read() 
    #create the cipher 
    cipher = Fernet(key)

    #open the file that needs to be encrypted 
    myfile = open("practiceData.csv", "rb")
    myfiledata = myfile.read() 

    #encrypt the data 
    encrypted_data = cipher.encrypt(myfiledata)
    #write the data to a file 
    edata = open("encrypted_file", "wb")
    edata.write(encrypted_data) 
    #print(encrypted_data)
    #open public key 
    public_keydata= open("publickey.key")
    public_key = RSA.import_key(public_keydata.read()) 


    #encrypting the symetric key file with the public RSA  key 
    encryptor = PKCS1_OAEP.new(public_key)
    encrypted_key = encryptor.encrypt(key) 

    #write the encrypted key to a file 
    ekey = open("encryptedkey", "wb")
    ekey.write(encrypted_key)

    ##print(encrypted_key)
    #used to benchmark runtime 
    print("Encryption took: " )
    print("--- %s seconds ---" % (time.time() - start_time))
