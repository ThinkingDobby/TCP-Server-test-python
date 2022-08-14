import os

from basic_test_server import BasicTestServer

# 사용 보류 - 헤더 타입 설정으로 대체 (type 2)

class FileTransferTestServerDS(BasicTestServer):
    def runServer(self):
        self.servSock.listen()
        self.clntSock, addr = self.servSock.accept()
        print("Client Address: ", addr)

        # 데이터 수신
        cwd = os.getcwd()
        with open(cwd + '/' + 'temp.wav', 'wb') as f:  # 파일명 - temp.wav 고정 (임시)
            while f.write(self.clntSock.recv(BasicTestServer.bufSize)):
                pass

        self.clntSock.sendall("Transfer Finished".encode())

        self.stopServer()


if __name__ == "__main__":
    basicTestServer = FileTransferTestServerDS()
    basicTestServer.runServer()
