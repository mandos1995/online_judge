lo = input()
x = int(ord(lo[0]) - 96)
y = int(lo[1])
count = 0
dx = [-2, -2, 2, 2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else:
        count += 1

print(count)