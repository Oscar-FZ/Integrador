import socket
import struct

#TEC - '172.21.255.137'
#CASITA - '192.168.1.34'



def init ():
    TCP_IP = '192.168.1.34'
    TCP_PORT = 10000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    return s

def send_message(string, s):
    s.send(string.encode())


def main():
    s = init()
    while True:
        string = str(input("Digite la opcion: "))
        if  (string == "exit"):
            s.close()
            break
        else:
            send_message(string, s)



#MAIN
main()
            
        
