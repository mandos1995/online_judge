n = int(input())
distance = list(map(int,input().split()))
city = list(map(int,input().split()))
del city[-1]
min_price_index = city.index(min(city))
sum = 0
for i in range(len(distance)):
    if i == min_price_index:
        for j in range(min_price_index, len(distance)):
            sum += city[min_price_index] * distance[j]
        break
    else:
        sum += distance[i] * city[i]
print(sum)