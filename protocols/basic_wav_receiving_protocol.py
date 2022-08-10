import os


class BasicWAVReceivingProtocol:
    def __init__(self, clntSock, bufSize):
        self._typ = -1
        self._fileSize = 0
        self._bufSize = bufSize
        self._clntSock = clntSock
        
    def get(self):
        baseData = self._clntSock.recv(self._bufSize)
        return baseData

    def save(self, baseData):
        self._typ = baseData[0]

        if self._typ == -1:
            print("Type Input Error")
        elif self._typ == 1:
            cwd = os.getcwd()
            with open(cwd + '/' + 'temp.wav', 'wb') as f:
                self._fileSize = self.getSize(baseData[1:5])
                data = baseData[5:]
                nowSize = len(data)
                f.write(data)

                while nowSize < self._fileSize:
                    data = self._clntSock.recv(self._bufSize)                    
                    if not data:
                        break
                    nowSize += len(data)
                    f.write(data)

                print(self._typ, self._fileSize, nowSize)

    # 4칸으로 나눠진 16진수 배열에서 파일 크기 계산해 반환
    def getSize(self, data):
        size = 0
        idx = 3
        for i in range(0, 7, 2):
            size += data[idx] * (16 ** i)
            idx -= 1
        return size

