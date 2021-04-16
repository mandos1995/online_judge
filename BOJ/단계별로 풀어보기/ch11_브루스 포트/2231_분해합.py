n = int(input())
sum = 0
count = 0
for i in range(1, n + 1):
    sum += i
    for j in str(i):
        sum += int(j)
    if n == sum:
        print(i)
        count += 1
        break
    else:
        sum = 0
if count == 0:
    print('0')
