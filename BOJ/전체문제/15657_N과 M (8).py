from itertools import combinations_with_replacement
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
for x in combinations_with_replacement(num, m):
    print(*list(x))