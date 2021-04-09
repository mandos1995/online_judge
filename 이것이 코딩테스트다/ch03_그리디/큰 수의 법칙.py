import sys
N, M, K = map(int,sys.stdin.readline().rstrip().split())
num = list(map(int,sys.stdin.readline().rstrip().split()))
num.sort(reverse=True)
sum = 0
while M > 0:
    for _ in range(K):
        if M == 0:
            break
        sum += num[0] * 1
        M -= 1
    if M == 0:
        break
    sum += num[1] * 1
    M -= 1
print(sum)