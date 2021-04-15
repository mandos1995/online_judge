n = int(input())
time = []
for _ in range(n):
    start, end = map(int, input().split())
    time.append([start, end])
time.sort(key = lambda x: x[0])
time.sort(key = lambda x: x[1])
# time.sort(key = lambda x: (x[1],x[0])) # 끝나는시간 x[1] 오름차순, 시작하는 시간 x[0] 오름차순

cnt = 1
end_time = time[0][1]
for i in range(1, n):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]
print(cnt)