import os


class BasicWAVReceivingProtocol:
    def __init__(self, clntSock, bufSize):
        self._typ = -1  # 전송 타입
        self._fileSize = 0  # 파일 전체 크기
        self._bufSize = bufSize
        self._clntSock = clntSock
        
    def get(self):
        # 최초 수신 데이터 (헤더 포함)
        baseData = self._clntSock.recv(self._bufSize)
        return baseData

    def save(self, baseData):
        # 타입 확인
        self._typ = baseData[0]

        # 오류 (임시)
        if self._typ == -1:
            print("Type Input Error")
        # 기본 수신
        elif self._typ == 1:
            cwd = os.getcwd()
            with open(cwd + '/' + 'temp.wav', 'wb') as f:   # 파일명 - temp.wav 고정 (임시)
                # 파일 크기 계산
                self._fileSize = self.getSize(baseData[1:5])
                # 헤더 제외 데이터
                data = baseData[5:]
                nowSize = len(data)
                f.write(data)

                # 저장
                while nowSize < self._fileSize:
                    data = self._clntSock.recv(self._bufSize)                    
                    if not data:
                        break
                    nowSize += len(data)
                    f.write(data)

                # print(self._typ, self._fileSize, nowSize)

    # 4바이트 연결해 파일 크기 계산 후 반환
    def getSize(self, data):
        size = 0
        idx = 3
        for i in range(0, 7, 2):
            size += data[idx] * (16 ** i)
            idx -= 1
        return size

