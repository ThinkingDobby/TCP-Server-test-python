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
        print(self._typ, header)

        # 임시 타입
        if self._typ == -1:
            print("temp type")
        # 기본 수신 - 파일로 저장
        elif self._typ == 1:
            # 파일 크기 계산
            self._fileSize = self.getSize(header[1:5])

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
        # 메모리에만 저장
        elif self._typ == 2:
            # 파일 크기 계산
            self._fileSize = self.getSize(header[1:5])

            nowSize = 0
            while True:
                data = self._clntSock.recv(self._bufSize)
                nowSize += len(data)
                if nowSize >= self._fileSize:
                    break
        elif self._typ == 3:
            cwd = os.getcwd()
            f = open(cwd + '/' + 'temp.pcm', 'wb')
            nowSize = 0
            # 저장
            while True:
                data = self._clntSock.recv(1024)
                print(data, end='')
                if data == b';;':
                    print()
                    print("FIN_CODE Received")
                    break
                nowSize += len(data)
                f.write(data)

            print(nowSize)

            f.flush()
            os.fsync(f)
            f.close()

    # 4바이트 연결해 파일 크기 계산 후 반환
    def getSize(self, data):
        size = 0
        idx = 3
        for i in range(0, 7, 2):
            size += data[idx] * (16 ** i)
            idx -= 1
        return size

