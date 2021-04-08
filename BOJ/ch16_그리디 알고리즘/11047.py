import sys
N, K = map(int,sys.stdin.readline().rstrip().split())
count = 0
coin_types = []
for _ in range(N):
    coin_types.append(int(sys.stdin.readline().rstrip()))
coin_types.sort(reverse=True)

for coin in coin_types:
    count += K // coin
    K = K % coin
print(count)