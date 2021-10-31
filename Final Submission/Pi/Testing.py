import glob
import os 
  
os.system('python3 SendData.py ' + "IMU-data.csv" )

os.system('python3 RecieveData.py' + " encrypted_fileofIMU.txt")