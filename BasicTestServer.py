import socket


class BasicTestServer:
    host = "127.0.0.1"
    port = 10001
    bufSize = 1024

    def __init__(self):
        self.servSock = None
        self.clntSock = None
        self.initSocket()

    def initSocket(self):
        self.servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.servSock.bind((BasicTestServer.host, BasicTestServer.port))

    def runServer(self):
        self.servSock.listen()
        self.clntSock, addr = self.servSock.accept()
        print("Client Address: " + addr)
        while True:
            data = self.clntSock.recv(BasicTestServer.bufSize).decode()
            if not data:
                break
            print("Received Data: " + data)

            # echoing
            self.clntSock.sendall(data.encode())
        self.stopServer()

    def stopServer(self):
        self.clntSock.close()
        self.servSock.close()


if __name__ == "__main__":
    basicTestServer = BasicTestServer()
    basicTestServer.runServer()
