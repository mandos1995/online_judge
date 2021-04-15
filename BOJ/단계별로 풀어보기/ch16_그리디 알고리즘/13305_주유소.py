n = int(input())
distance = list(map(int,input().split()))
city = list(map(int,input().split()))
sum = 0
min = city[0]
for i in range(len(distance)):
    if city[i] < min:
        min = city[i]
    sum += min * distance[i]
print(sum)