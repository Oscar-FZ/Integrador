import socket
import struct
import time

envio_str = 'Hola Mun2!'

#TCP_IP = '192.168.1.40'
TCP_IP = '172.21.255.137'
TCP_PORT = 10000

while(envio_str != 'exit'):
    envio_str = str(input("Escriba el mensaje que quiera mandar: "))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(envio_str.encode())
    time.sleep(1)
    s.close()


######################################################################
#3C:6A:A7:3D:86:95
#server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
#server.bind(("3C:6A:A7:3D:86:95", 4))
#server.listen(1)

#client, addr = server.accept()

#try:
#    while True:
#        data = client.recv(1024)
#        if no data:
#            break
#        print(f"Message: {data.decode('utf-8')}")
#        message = input("Enter message: ")
#        client.send(message.encode(utf-8))
#
#except OSError as e:
#    pass
#
#client.close()
#server.close()
