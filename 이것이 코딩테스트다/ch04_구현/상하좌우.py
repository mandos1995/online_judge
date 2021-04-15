n = int(input())
location = list(map(str, input().split()))
x = 1
y = 1
for i in location:
    if i == 'R':
        if y >= n:
            continue
        else:
            y += 1
    if i == 'L':
        if y <= 1:
            continue
        else:
            y -= 1
    if i == 'U':
        if x <= 1:
            continue
        else:
            x -= 1
    if i == 'D':
        if x >= n:
            continue
        else:
            x += 1
print(x,y)