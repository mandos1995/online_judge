T = int(input())
for i in range(T):
    k = int(input()) # 층
    n = int(input()) # 호
    f0 = [x for x in range(1, n+1)] # 0층
    for j in range(k):
        for k in range(1,n):
            f0[k] += f0[k-1]
    print(f0[-1])

