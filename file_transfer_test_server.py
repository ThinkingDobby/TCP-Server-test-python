import os

from basic_test_server import BasicTestServer


class FileTransferTestServer(BasicTestServer):
    def runServer(self):
        self.servSock.listen()
        self.clntSock, addr = self.servSock.accept()
        print("Client Address: ", addr)

        size = self.clntSock.recv(BasicTestServer.bufSize).decode()
        size = int(size)
        cwd = os.getcwd()
        with open(cwd + '/' + 'temp.wav', 'wb') as f:
            while True:
                data = self.clntSock.recv(BasicTestServer.bufSize)
                if not data:
                    break
                else:
                    f.write(data)

        print('size: %d' % size)
        self.clntSock.sendall("Transfer Finished".encode())

        self.stopServer()


if __name__ == "__main__":
    basicTestServer = BasicTestServer()
    basicTestServer.runServer()
