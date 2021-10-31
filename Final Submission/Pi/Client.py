import socket
import SendData 
import os 
from Crypto.PublicKey import RSA  
from Crypto.Cipher import PKCS1_OAEP

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 12345        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b'Hello, world')
    #line below receieves data from server and decodes it 
    keydata = RSA.importKey(s.recv( 1024 ), passphrase=None) 
    with open('Publickey.key','wb') as f:
     f.write(keydata.export_key('PEM'))
    print('Received RSA key')
   
    print(len(open("Publickey.key", "rb").read()))
    SendData.sendData("IMU-data.csv")
    #will send across the e crypted key 
    q = open("encryptedkey", "rb")
    print ("key length=" , (len(open("encryptedkey", "rb").read())))
    key = q.read()
    print(len(key))
    print("sending encrypted key")
    s.send(key)

    #the file is opened and sent 
    p = open("encrypted_fileofIMU.txt" , "rb")
    data = p.read()
    print("Sending data to laptop")
    s.sendall(data)
    s.close() 


     
    #
    


