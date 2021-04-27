from itertools import product
n, m = map(int, input().split())
num = []
for i in range(1, n + 1):
    num.append(i)
for x in product(num, repeat = m):
    print(*x)