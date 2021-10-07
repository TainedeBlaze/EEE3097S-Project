from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA  
from Crypto.Cipher import PKCS1_OAEP
import time 
import sys

compressed_files = ['compressedData_of_2018-09-19-03_57_11_VN100.csv', 'compressedData_of_2018-09-19-04_22_21_VN100.csv', 'compressedData_of_2018-09-19-06_28_11_VN100.csv', 'compressedData_of_2018-09-19-06_53_21_VN100.csv', 'compressedData_of_2018-09-19-08_59_11_VN100.csv', 'compressedData_of_2018-09-19-09_24_21_VN100.csv', 'compressedData_of_2018-09-19-09_49_31_VN100.csv', 'compressedData_of_2018-09-19-11_55_21_VN100.csv', 'compressedData_of_2018-09-19-12_20_31_VN100.csv']

def main():
    for i in compressed_files:
        print(i)
        eout = open('eTest.txt_of_' + i + '.txt', 'ab')

        eout.write(encrypt(i))
        eout.close()

def encrypt(text):
    start_time = time.time()
    #open the symetric key file 
    skey = open("symetricKey.key" , "rb" )
    key = skey.read() 

    #create the cipher 
    cipher = Fernet(key)

    #open the file that needs to be encrypted 
    #myfile = open(text, "rb")
   #myfiledata = myfile.read() 
    myfiledata = text 
    #encrypt the data 
    encrypted_data = cipher.encrypt(myfiledata)
 
    #write the data to a file 
    edata = open("encrypted_fileof.txt", "wb")
    edata.truncate(0)
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
    ekey.truncate(0)
    ekey.write(encrypted_key)

    ##print(encrypted_key)
    #used to benchmark runtime 
    print("Encryption took: " )
    print("--- %s seconds ---" % (time.time() - start_time))

    #returning the encrytped file:
    return encrypted_data



