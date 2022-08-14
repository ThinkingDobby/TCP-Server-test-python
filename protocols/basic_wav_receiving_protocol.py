import os


class BasicWAVReceivingProtocol:
    def __init__(self, clntSock, bufSize):
        self._typ = -1  # 전송 타입
        self._fileSize = 0  # 파일 전체 크기
        self._bufSize = bufSize
        self._clntSock = clntSock
        
    def getHeader(self):
        # 헤더 수신
        header = self._clntSock.recv(5)
        return header

    def save(self, header):
        # 타입 확인
        self._typ = header[0]
        # 파일 크기 계산
        self._fileSize = self.getSize(header[1:5])
        # print(self._typ, self._fileSize)

        # 오류 (임시)
        if self._typ == -1:
            print("Type Input Error")
        # 기본 수신
        elif self._typ == 1:
            cwd = os.getcwd()
            with open(cwd + '/' + 'temp.wav', 'wb') as f:   # 파일명 - temp.wav 고정 (임시)
                nowSize = 0
                # 저장
                while True:
                    data = self._clntSock.recv(self._bufSize)
                    nowSize += len(data)
                    f.write(data)
                    if nowSize >= self._fileSize:
                        break
        # 파일에 바로 저장
        elif self._typ == 2:
            cwd = os.getcwd()
            with open(cwd + '/' + 'temp.wav', 'wb') as f:
                while f.write(self._clntSock.recv(self._bufSize)):
                    pass
        # 푸리에 변환 적용 테스트 - 텍스트 파일에 저장
        elif self._typ == 3:
            cwd = os.getcwd()
            with open(cwd + '/' + 'temp.txt', 'wb') as f:
                nowSize = 0
                while True:
                    data = self._clntSock.recv(self._bufSize)
                    nowSize += len(data)
                    f.write(data)
                    if nowSize >= self._fileSize:
                        break

    # 4바이트 연결해 파일 크기 계산 후 반환
    def getSize(self, data):
        size = 0
        idx = 3
        for i in range(0, 7, 2):
            size += data[idx] * (16 ** i)
            idx -= 1
        return size

