# 내가 푼 방식
N, M = map(int, input().split())
num = []
for _ in range(N):
    data = list(map(int, input().split()))
    data.sort()
    num.append(data[0])
print(max(num))
