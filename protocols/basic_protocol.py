class BasicProtocol:
    def __init__(self):
        self.typ = -1
        self.size = 0

    def save(self, data):
        self.typ, self.size = self.getInfo(data)

        if self.typ == -1:
            print("Type Input Error")


    def getInfo(self, data):
        typ = data[0]
        size = self.getSize(data[1:5])
        return typ, size

    def getSize(self, data):
        size = 0
        idx = 3
        for i in range(0, 7, 2):
            print(size)
            size += data[idx] * (16 ** i)
            idx -= 1
        return size

