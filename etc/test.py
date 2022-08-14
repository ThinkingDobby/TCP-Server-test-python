# for i in range(11):
#     data = input().rstrip()
#     print(data[-8:])

# 각 길이에 대해 평균의 차의 평균
# sum_v = 0
# for i in range(5):
#     f, s = map(float, input().split())
#     sum_v += f - s
#
# print(sum_v / 5)

# 각 길이에 대해 평균의 /의 평균
sum_v = 0
for _ in range(5):
    a, b = map(float, input().split())
    sum_v += b / a

print(sum_v / 5)