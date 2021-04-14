import math
n = int(input())
num_list = list(map(int,input().split()))
count = 0
for num in num_list:
    if num == 1:
        count += 1
    else:
        for i in range(2,int(math.sqrt(num)) + 1):
            if num % i == 0:
                count += 1
                break
print(n - count)
