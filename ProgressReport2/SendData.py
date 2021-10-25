import create_keys
import Encrypt_data 
import Decrypt_data 
import Compression 
import Decompression 
import os 
import sys
import time 

def sendData(text):
   start_time = time.time()
   #first create the keys used for 
   create_keys.createkeys()  
   
   #compresses data past into function 
   compressed_data = Compression.compress(text)

   #Encrypt the data that has been compressed 
   Encrypt_data.encrypt(compressed_data)
   print("The time to compress and encrypt together took: ")
   print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__": 

   inputfile = sys.argv[1]
   sendData(sys.argv[1])    