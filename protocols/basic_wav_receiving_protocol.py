import os
from pathlib import Path


class BasicWAVReceivingProtocol:
    cnt = 10

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
        print(self._typ)
        # 파일 크기 계산
        self._fileSize = self.getSize(header[1:5])
        # print(self._typ, self._fileSize)

        # 오류 (임시)
        if self._typ == -1:
            print("Type Input Error")
        # 기본 수신
        elif self._typ == 1:
            cwd = os.getcwd()
            f = open(cwd + '/' + 'temp.wav', 'wb')   # 파일명 - temp.wav 고정 (임시)
            nowSize = 0
            # 저장
            while True:
                data = self._clntSock.recv(self._bufSize)
                nowSize += len(data)
                f.write(data)
                if nowSize >= self._fileSize:
                    break
            f.flush()
            os.fsync(f)
            f.close()
            self.checkFile(cwd + '/' + 'temp.wav', self._fileSize)
            if BasicWAVReceivingProtocol.cnt > 0:
                if BasicWAVReceivingProtocol.cnt == 1:
                    self._clntSock.sendall("Transfer Finished".encode())
                else:
                    self._clntSock.sendall("Transferred".encode())
                    BasicWAVReceivingProtocol.cnt -= 1
        # 메모리에만 저장
        elif self._typ == 2:
            nowSize = 0
            while True:
                data = self._clntSock.recv(self._bufSize)
                nowSize += len(data)
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

    def checkFile(self, path, size):
        file = Path(path)
        while True:
            # print(file.stat().st_size, self._fileSize)
            if file.exists() and file.stat().st_size >= size:
                break

