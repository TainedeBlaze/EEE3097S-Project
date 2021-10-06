# Zlib compression algorithm for csv data files.
# Script written by Michael Altshuler (ALTMIC003) and Taine de Buys (DBYTAI001)

import zlib, sys, time, base64;
import binascii

data = ['2018-09-19-03_57_11_VN100.csv', '2018-09-19-04_22_21_VN100.csv', '2018-09-19-06_28_11_VN100.csv', '2018-09-19-06_53_21_VN100.csv', '2018-09-19-08_59_11_VN100.csv', '2018-09-19-09_24_21_VN100.csv', '2018-09-19-09_49_31_VN100.csv', '2018-09-19-11_55_21_VN100.csv', '2018-09-19-12_20_31_VN100.csv']

#main function executes compress() and then in turn appends the result of each compressed file to a new text file to then be encrypted.
def main():
    for i in data:
        print(i)
        output = open('compressedData' + '_of_' + i + '.txt', 'ab')
        output.write(compress(i))
        output.close()

#function serves the purpose of compressing any incoming .csv files.
def compress(file):
    with open(file, 'rb') as fileobj:
        file = fileobj.read()
    
    #print statements compare the original size of the data set to the size of the compressed data (in bytes)
    print("Raw data size: ", sys.getsizeof(file))

    compressed = base64.b64encode(zlib.compress(file, 9))
    print("Compressed data file size: ", sys.getsizeof(compressed))

    return compressed

if __name__ == "__main__":
    main()