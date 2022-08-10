import os

from basic_test_server import BasicTestServer
from protocols.basic_protocol import BasicProtocol


class FileTransferTestServer(BasicTestServer):
    def runServer(self):
        self.servSock.listen()
        self.clntSock, addr = self.servSock.accept()
        print("Client Address: ", addr)

        cwd = os.getcwd()
        pt = BasicProtocol()
        with open(cwd + '/' + 'temp.wav', 'wb') as f:
            data = self.clntSock.recv(BasicTestServer.bufSize)
            data = data[5:]

            while True:
                f.write(data)
                data = self.clntSock.recv(BasicTestServer.bufSize)
                if not data:
                    break

        self.clntSock.sendall("Transfer Finished".encode())

        self.stopServer()


if __name__ == "__main__":
    basicTestServer = FileTransferTestServer()
    basicTestServer.runServer()
