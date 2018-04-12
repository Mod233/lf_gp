from socket import *

def server_listen():
    print "Please input the port you choose!"
    port = int(raw_input())
    bufsiz = 2048
    tcpSerSocket = socket(AF_INET, SOCK_STREAM)
    server_addr = ("127.0.0.1", port)
    tcpSerSocket.bind(server_addr)
    tcpSerSocket.listen(5)
    while True:
        print "waiting for connection from client..."
        tcpCliSocket, addr = tcpSerSocket.accept()
        print "...connected from: ", addr
        size = int(0)
        name = tcpCliSocket.recv(bufsiz, size)
        print "file name is ", name
        name = "get_from_client-" + name
        f = open(name, "wb")
        while True:
            data = tcpCliSocket.recv(bufsiz)
            if not data:
                break
            while data:
                f.write(data)
        f.close()
    tcpSerSocket.close()
    tcpCliSocket.close()


if __name__ == "__main__":
    server_listen()

