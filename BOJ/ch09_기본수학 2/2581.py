# 에라토스테네스의 체 알고리즘을 사용
import math
n = int(input())
m = int(input())
num = [] # 소수
array = [True for i in range(10001)]

for i in range(2, int(math.sqrt(10000)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= 10000:
            array[i * j] = False
            j += 1

for i in range(n, m + 1):
    if i == 1:
        continue
    if array[i]:
        num.append(i)

if len(num) == 0:
    print(-1)
else:
    print(sum(num))
    print(min(num))

