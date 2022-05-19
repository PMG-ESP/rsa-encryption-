import socket
import rsa
import pickle
import time

#creation des cles

publicKey,privateKey = rsa.newkeys(1024)
with open('key1.txt','wb') as key:
    pickle.dump(publicKey,key,pickle.HIGHEST_PROTOCOL)

print("Recuperation de la cle...")
with open('key2.txt','rb') as key:
    foreignKey = pickle.load(key)
print("ok")

message = "Hello world"
cryptedMessage = rsa.encrypt(message.encode("utf8"), foreignKey)

mySock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mySock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host,port = "0.0.0.0",6666
mySock.bind((host,port))
mySock.listen()

try:
    print("waiting for the client")
    client,addr = mySock.accept()
    print(f"client: {addr} connecte !")
except socket.error as e:
    print(f"Erreur connexion client: {e}")
    mySock.close()

client.sendall(cryptedMessage)

client.close()
mySock.close()






#print(publicKey)
# print("----------------------------------")
# print(cryptedMessage)
# print("----------------------------------")
#print(rsa.decrypt(cryptedMessage, privateKey))