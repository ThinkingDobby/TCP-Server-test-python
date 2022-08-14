memo = []
for _ in range(10):
    data = input().rstrip()
    memo.append(int(data[-8]) * 10**6 + int(data[-6:]))
    print(data[-8], data[-6:])

print(round((sum(memo) / 10) * 10**-6, 6))
