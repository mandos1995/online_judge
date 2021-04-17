n = int(input())
location = []
for _ in range(n):
    location.append(list(map(int, input().split())))
location.sort(key=lambda x: (x[1], x[0]))
for i in range(len(location)):
    print(location[i][0], location[i][1])