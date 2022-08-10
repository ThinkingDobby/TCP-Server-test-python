import os

from basic_test_server import BasicTestServer
from protocols.basic_wav_receiving_protocol import BasicWAVReceivingProtocol


class FileTransferTestServer(BasicTestServer):
    def runServer(self):
        self.servSock.listen()
        self.clntSock, addr = self.servSock.accept()
        print("Client Address: ", addr)

        pt = BasicWAVReceivingProtocol(self.clntSock, BasicTestServer.bufSize)
        baseData = pt.get()
        pt.save(baseData)

        self.clntSock.sendall("Transfer Finished".encode())

        self.stopServer()


if __name__ == "__main__":
    basicTestServer = FileTransferTestServer()
    basicTestServer.runServer()
