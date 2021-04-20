n = int(input())
i = 0
count = 0
while True:
    i += 1
    if str(i).count('666') >= 1:
        count += 1
    if n == count:
        break
print(i)