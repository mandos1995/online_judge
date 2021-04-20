n = int(input())
heavy = []
for _ in range(n):
    heavy.append(list(map(int, input().split())))
for i in heavy:
    rank = 1
    for j in heavy:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')