from socket import *
from time import *

def client_connect():
    host = 'localhost'
    bufsiz = 2048
    print "Please input the port you choose!"
    port = int(raw_input())
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)
    server_addr = (host, port)
    tcp_client_socket.connect(server_addr)
    print "please in put the file name"
    filename = raw_input()
    sleep(5)
    f = open(filename, "rb")
    tcp_client_socket.send(filename)
    data = f.read(bufsiz)
    while data:
        tcp_client_socket.send(data)
        data = f.read(bufsiz)
    tcp_client_socket.close()

if __name__ == "__main__":
    client_connect()
