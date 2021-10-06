# Program designed to benchmark the compression and decompression algorithms.
# Script written by Michael Altshuler (ALTMIC003) and Taine de Buys (DBYTAI001)

import zlib, sys, time, base64;

data = ['2018-09-19-03_57_11_VN100.csv', '2018-09-19-04_22_21_VN100.csv', '2018-09-19-06_28_11_VN100.csv', '2018-09-19-06_53_21_VN100.csv', '2018-09-19-08_59_11_VN100.csv', '2018-09-19-09_24_21_VN100.csv', '2018-09-19-09_49_31_VN100.csv', '2018-09-19-11_55_21_VN100.csv', '2018-09-19-12_20_31_VN100.csv']

def main():
    for n in data:
        print('Looking at file: ', n)
        benchmark(n)


def benchmark(file):
    data = ['2018-09-19-03_57_11_VN100.csv', '2018-09-19-04_22_21_VN100.csv', '2018-09-19-06_28_11_VN100.csv', '2018-09-19-06_53_21_VN100.csv', '2018-09-19-08_59_11_VN100.csv', '2018-09-19-09_24_21_VN100.csv', '2018-09-19-09_49_31_VN100.csv', '2018-09-19-11_55_21_VN100.csv', '2018-09-19-12_20_31_VN100.csv']

    with open(file, 'rb') as fileobj:
        file = fileobj.read()
    
    print("Raw data size of: ", sys.getsizeof(file))

    #level of compression: 0 = none, 1-9 is increasing intensity with decreased runtime.
    for i in range(0,10,1):
        startt = time.time()
        code = base64.b64encode(zlib.compress(file, i))
        compTime = time.time() - startt
        data = zlib.decompress(base64.b64decode(code))
        fullTime = time.time() - startt

        print('Compressed size of ' + str(i) + ': ', sys.getsizeof(code), '. Time took: ', compTime, '.', 'Ratio is: ', float(sys.getsizeof(code)/sys.getsizeof(file)), '.')
        print('Full compression and decompression time: ', fullTime)
        print('')


if __name__ == '__main__':
    main()