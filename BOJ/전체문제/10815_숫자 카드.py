n = int(input())
card = set(map(str, input().split())) # 시간초과가 나서 list를 set으로 변경하여 품
m = int(input())
check = list(map(str, input().split()))
output = [0] * m

for i in range(m):
    if check[i] in card:
        output[i] = 1

print(*output)

# 이분탐색에 대한 공부가 더 필요할거 같다.. 다 까먹음