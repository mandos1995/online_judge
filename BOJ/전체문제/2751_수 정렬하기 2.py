N = int(input())
sort_list = []
for i in range(N):
    sort_list.append(int(input()))

sort_list = sorted(sort_list)
for i in range(len(sort_list)):
    print(sort_list[i])