#import necessary keys 

import socket 
from Crypto.PublicKey import RSA 
import os
import sys
import io 
import time

print(socket.gethostname())

def make_key(): 
    start_time = time.time() 
    #Creatng rsa public and private keys
    keyPair= RSA.generate(1024)
    pubKey = keyPair.publickey() 

    #writing public key to file 
    p = open("Publickey.key" , "wb")
    pubKeyPEM = pubKey.exportKey()
    p.write(pubKeyPEM)
    p.close() 

    #writing private key in file 
    pr = open("Privatekey.Key", "wb")
    privKeyPEM = keyPair.exportKey() 
    pr.write(privKeyPEM)
    pr.close() 
    print("The time to create keys took: ")
    print("--- %s seconds ---" % (time.time() - start_time))


HOST = '127.0.0.1' # Standard loopback interface address (localhost)
PORT = 12345        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #this creates a socket of type IPV4 and Sock_STream means TCP connection 
    s.bind((HOST, PORT)) 
    s.listen() #allows for server to wait for connections 
    conn, addr = s.accept() #blocks the rest and waitts for a client to connect, once this happens it populates the values on the left 
    make_key() 
    print(len(open("Publickey.key", "rb").read()))
    with conn:
        p = open("Publickey.key" , "rb")
        keydata = p.read(1024)
        conn.sendall(keydata)
        print('Connected by', addr)
        encryptedkey = conn.recv(128)
        with open ("encryptedkey" , "wb") as key: 
            key.truncate(0)
            key.write(encryptedkey)
        print("key recieved")
        print (len(open("encryptedkey", "rb").read()))

        data = conn.recv(1500000) #this waits to recieve the data sent by the client 
        with open ("encrypted_fileofIMU.txt" , "wb") as r: 
            r.write(data)
        print("data recieved")     
        os.system('python3 RecieveData.py' + " encrypted_fileofIMU.txt")             



