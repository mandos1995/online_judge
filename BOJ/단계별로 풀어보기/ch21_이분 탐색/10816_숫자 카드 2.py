from collections import Counter

n = int(input())
input_list = list(map(int,input().split()))

m = int(input())
input_list2 = list(map(int,input().split()))

count = Counter(input_list)

for i in input_list2:
    print(count[i], end=' ')