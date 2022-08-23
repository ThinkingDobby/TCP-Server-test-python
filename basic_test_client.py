import socket


# 플러터 앱 구현 전 테스트용 클라이언트
class BasicTestClient:
    host = "192.168.35.69"    # x1
    port = 10001
    bufSize = 1024

    def __init__(self):
        self.clntSock = None
        self.initSocket()

    def initSocket(self):
        self.clntSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def setServAddr(self, host, port):
        BasicTestClient.host = host
        BasicTestClient.port = port

    def sendRequest(self):
        self.clntSock.connect((BasicTestClient.host, BasicTestClient.port))

    def sendData(self):
        while True:
            data = input("Data: ")
            self.clntSock.sendall(data.encode())
            if not data:
                break

            receivedData = self.clntSock.recv(BasicTestClient.bufSize).decode()
            print("Received Data: " + receivedData)

        self.stopClnt()

    def stopClnt(self):
        self.clntSock.close()


if __name__ == "__main__":
    basicTestServer = BasicTestClient()
    basicTestServer.sendRequest()
    basicTestServer.sendData()
