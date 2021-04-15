import math
import sys
n = int(input())
if n == 1:
    sys.exit()
num = [] # 소수

array = [True for i in range(10000001)]

for i in range(2, int(math.sqrt(10000000)) + 1):
    if array[i]:
        j = 2
        while i * j <= 10000:
            array[i * j] = False
            j += 1

for i in range(2, n + 1):
    if i == 1:
        continue
    if array[i]:
        num.append(i)

start = 0
while True:
    if n // num[start] == 1 and n % num[start] == 0:
        print(num[start])
        break
    if n % num[start] == 0:
        print(num[start])
        n = n // num[start]
    else:
        start += 1