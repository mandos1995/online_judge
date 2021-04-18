import collections
n = int(input())
n_list = []
for _ in range(n):
    n_list.append(int(input()))
# 평균
print(round(sum(n_list)/len(n_list)))

# 중앙값
n_list.sort()
print(n_list[n//2])

# 최빈값
k = collections.Counter(n_list).most_common()
if len(n_list) > 1: # 입력값이 1개이면 예외
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else:
        print(k[0][0])
else:
    print(n_list[0])

# 범위
print(n_list[-1] - n_list[0])