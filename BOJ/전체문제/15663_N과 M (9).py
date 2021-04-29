from itertools import permutations
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
empty = []
for x in permutations(num, m):
    empty.append(x)
empty = list(set(empty))
empty.sort()
for i in range(len(empty)):
    print(*empty[i])