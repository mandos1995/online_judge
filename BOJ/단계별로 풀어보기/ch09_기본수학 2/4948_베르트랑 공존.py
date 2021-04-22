import math
array = [True for i in range(256913)]
n = 1
for i in range(2, int(math.sqrt(256912)) + 1):
    if array[i]:
        j = 2
        while i * j <= 256912:
            array[i * j] = False
            j += 1
while n != 0:
    count = 0
    n = int(input())
    for i in range(n + 1, (2 * n) + 1):
        if array[i]:
            count += 1
    if n != 0:
        print(count)
