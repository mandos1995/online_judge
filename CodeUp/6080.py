dice1, dice2 = map(int, input().split())
for i in range(1, dice1 + 1):
    for j in range(1, dice2 + 1):
        print(i, j)