import os


class BasicWAVReceivingProtocol:
    def __init__(self, clntSock, bufSize):
        self._typ = -1  # 전송 타입
        self._bufSize = bufSize
        self._clntSock = clntSock
        
    def getHeader(self):
        # 헤더 수신
        header = self._clntSock.recv(2)
        return header

    def save(self, header):
        # 시작코드 확인
        if header[0:1] != b'[':
            print("Start Code Error")

        # 타입 확인
        self._typ = header[1]

        # wav파일 수신
        if self._typ == 1:
            # 헤더 모두 수신 (총 10바이트)
            header += self._clntSock.recv(8)
            # 메시지 크기
            msgSize = header[2]
            # 확장자
            ext = header[3:6]
            # 파일 크기
            fileSize = self.getSize(header[6:10])

            cwd = os.getcwd()
            f = open(cwd + '/' + 'temp.wav', 'wb')   # 파일명 - temp.wav 고정 (임시)
            nowSize = 0
            # 저장
            while True:
                data = self._clntSock.recv(self._bufSize)
                nowSize += len(data)

                if nowSize >= fileSize:
                    f.write(data[:fileSize - nowSize])
                    # 종료코드 확인
                    if data[fileSize - nowSize:] != b']':
                        print("End Code Error")
                    break

                f.write(data)

            f.flush()
            os.fsync(f)
            f.close()
        # pcm파일 실시간 수신
        elif self._typ == 2:
            pass

    # 4바이트 연결해 파일 크기 계산 후 반환
    def getSize(self, data):
        size = 0
        idx = 3
        for i in range(0, 7, 2):
            size += data[idx] * (16 ** i)
            idx -= 1
        return size

