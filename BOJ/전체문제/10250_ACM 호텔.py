T = int(input())
for i in range(T):
    first = 0
    second = 1
    H, W, N = map(int,input().split())
    for j in range(N):
        if first == H:
            first = 0
            second += 1
        first += 1
    if len(str(second)) == 1:
        print(str(first)+'0'+str(second))
    else:
        print(first,second,sep='')

