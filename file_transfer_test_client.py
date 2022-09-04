import socket
import numpy as np


# 서버에 파일을 전송하고 반환값을 받는 클라이언트
class FileTransferTestClient:
    def __init__(self):
        self.host = "192.168.35.243"
        self.port = 10001
        self.bufSize = 1024
        
        self.clientSock = None
        self.initSocket()
        
    # 소켓 초기화
    def initSocket(self):
        self.clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    # 연결 요청
    def sendRequest(self):
        self.clientSock.connect((self.host, self.port))

    # 파일 전송
    def sendFile(self, typ, data):
        if typ == 1 or typ == 2:
            # 타입
            typ = np.array(typ).astype('uint8').tobytes()
            # 파일 크기
            msgSize = len(data).to_bytes(4, byteorder="big", signed=False)

            # 타입과 파일 크기로 헤더 구성
            header = typ + msgSize
            # 헤더와 파일 전송
            self.clientSock.sendall(header + data)

            # 반환값 수신
            msgFromServer = self.clientSock.recv(self.bufSize)
            print(msgFromServer.decode("utf-8"))

            self.stopClient()
    
    # 클라이언트 종료
    def stopClient(self):
        self.clientSock.close()


if __name__ == "__main__":
    fileName = "input.wav"  # 임시 파일명: 전송-input.wav, 저장-temp.wav
    typ = 1

    try:
        with open(fileName, "rb") as f:
            # 파일 내용 로드
            data = f.read()

            client = FileTransferTestClient()
            client.sendRequest()

            client.sendFile(typ, data)
    except FileNotFoundError:
        print("File not exists: " + fileName)
