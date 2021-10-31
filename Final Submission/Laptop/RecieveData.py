import Encrypt_data 
import Decrypt_data 
import Decompression 
import os 
import sys
import time 


def recieveData(text): 
   start_time = time.time()
   #decrypt the data that has been compressed 
   Decrypt_data.decrypt(text) 

   #decompress
   Decompression.decompress("decrypted_data", text)
   print("The to decrypt and decompress together took:")
   print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__": 

   inputfile = sys.argv[1]
    
   recieveData(inputfile)