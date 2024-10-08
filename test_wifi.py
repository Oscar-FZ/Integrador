import socket
import struct
import time

envio_str = 'Wenas!'

TCP_IP = '192.168.1.40'
TCP_PORT = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(envio_str.encode())
time.sleep(3)
s.close()
