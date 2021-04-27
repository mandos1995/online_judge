from itertools import combinations_with_replacement
n, m = map(int, input().split())
num = []
for i in range(1, n + 1):
    num.append(i)
for x in combinations_with_replacement(num, m):
    print(*x)