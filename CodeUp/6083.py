import sys
r, g, b = map(int, sys.stdin.readline().split())
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k,sep=' ')
print(r*g*b)