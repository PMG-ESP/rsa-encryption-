import socket
import rsa
import pickle
import time
import os

publicKey, privateKey = rsa.newkeys(1024)
with open("key2.txt","wb") as key2:
    pickle.dump(publicKey,key2,pickle.HIGHEST_PROTOCOL)
time.sleep(5)


mySock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


try:
    mySock.connect(("0.0.0.0",6666))
except socket.error as e:    
    print(f"Erreur connexion au serveur {e}")
    mySock.close()

message = mySock.recv(1024)
try:
    decryptedMessage = rsa.decrypt(message, privateKey)
finally:
    os.remove("key1.txt")
    os.remove("key2.txt")

print(decryptedMessage)


