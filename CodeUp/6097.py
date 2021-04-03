h, w = map(int,input().split())
n = int(input())
table = [[0 for i in range(w)] for j in range(h)]

for i in range(n):
    l, d, x, y = map(int,input().split())
    for i in range(l):
        if d == 0:
            table[x-1][y-1+i] = 1
        else:
            table[x-1+i][y-1] = 1

for i in range(h):
    for j in range(w):
        print(table[i][j],end=' ')
    print()