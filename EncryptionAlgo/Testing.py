import glob
import os 
  
# specifying the path to csv files
#path = "CSV_Files"

data = ['2018-09-19-03_57_11_VN100.csv', '2018-09-19-04_22_21_VN100.csv', '2018-09-19-06_28_11_VN100.csv', '2018-09-19-06_53_21_VN100.csv', '2018-09-19-08_59_11_VN100.csv', '2018-09-19-09_24_21_VN100.csv', '2018-09-19-09_49_31_VN100.csv', '2018-09-19-11_55_21_VN100.csv', '2018-09-19-12_20_31_VN100.csv']
compressed_files = ['compressedData_of_2018-09-19-03_57_11_VN100.csv.txt', 'compressedData_of_2018-09-19-04_22_21_VN100.csv.txt', 'compressedData_of_2018-09-19-06_28_11_VN100.csv.txt', 'compressedData_of_2018-09-19-06_53_21_VN100.csv.txt', 'compressedData_of_2018-09-19-08_59_11_VN100.csv.txt', 'compressedData_of_2018-09-19-09_24_21_VN100.csv.txt', 'compressedData_of_2018-09-19-09_49_31_VN100.csv.txt', 'compressedData_of_2018-09-19-11_55_21_VN100.csv.txt', 'compressedData_of_2018-09-19-12_20_31_VN100.csv.txt']

# csv files in the path
#files = glob.glob(path + "/*.csv")
#Changed to test different functions 
for i in compressed_files: 
    os.system('python3 main.py ' +i )