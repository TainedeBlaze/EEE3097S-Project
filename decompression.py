# Zlib decompression algorithm for csv data files.
# Script written by Michael Altshuler (ALTMIC003) and Taine de Buys (DBYTAI001)

import zlib, sys, time, base64;
import binascii
import compression

#main function executes decompress() function, and further appends the decompressed data to new text files.
def main():
    for i in compression.data:
        decompress('compressedData' + '_of_' + i + '.txt')
        
        #Creating a new text file to which the decompressed data is sent.
        decompressed_output = open('decompressedData_of_' + i + '.txt', 'ab')
        decompressed_output.write(decompress('compressedData_of_' + i + '.txt'))
        decompressed_output.close()
        print("Successful decompression. Output file: " + i)


#function that serves the purpose of decompressing incoming decrypted compressed files.
def decompress(compressed_data):
    with open(compressed_data, 'rb') as fileobj:
        compressed_data = fileobj.read()
    
    decompressed = zlib.decompress(base64.b64decode(compressed_data))

    return decompressed 

if __name__ == "__main__":
    main() 