from difflib import Differ
  
with open('IMU-data-2021-10-25-19:35:45.txt') as file_1, open('decompressedData_of_encrypted_fileofIMU.txt.txt') as file_2:
    differ = Differ()
  
    for line in differ.compare(file_1.readlines(), file_2.readlines()):
        print(line)