n = int(input())
info = []
for _ in range(n):
    info.append(list(map(str, input().split())))
info.sort(key=lambda x: int(x[0]))
for i in range(len(info)):
    print(info[i][0],info[i][1])