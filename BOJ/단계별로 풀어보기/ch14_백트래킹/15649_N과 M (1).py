import itertools
n, m = map(int, input().split())
num = []
for i in range(1, n + 1):
    num.append(i)
for x in itertools.permutations(num, m):
    print(*list(x))