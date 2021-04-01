num = int(input())
start = 0
sep = 1
while True:
    start += sep
    sep += 1
    if start >= num:
        break
print(start)