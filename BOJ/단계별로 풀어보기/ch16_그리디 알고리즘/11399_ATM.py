N = int(input())
time = list(map(int, input().split()))
time = sorted(time)
list_sum = []
min_time = 0
for i in range(len(time)):
    list_sum.append(time[i])
    min_time = min_time + sum(list_sum)
print(min_time)