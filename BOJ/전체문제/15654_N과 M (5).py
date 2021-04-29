from itertools import permutations
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
for x in permutations(num, m):
    print(*list(x))