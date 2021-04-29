from itertools import combinations
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
for x in combinations(num, m):
    print(*list(x))