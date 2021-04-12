# 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘

# 1. 시작점(start)과 끝점(end)이 첫번째 원소의 인덱스(0)를 가리키도록 한다.
# 2. 현재 부분합이 M과 같다면 카운트한다.
# 3. 현재 부분합이 M보다 작으면 end를 1 증가시킨다.
# 4. 현재 부분합이 M보다 크거나 같으면 start를 1 증가시킨다.
# 5. 모든 경우를 확인할 때까지 2 ~ 4 까지의 과정을 반복한다.

# 부분합이 5 가 되는 경우

n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가사키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)

# 정렬되어 있는 두 리스트의 합집합 문제 활용

# 사전에 정렬된 리스트 A와 B 선언
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

# 리스트 A와 B의 모든 원소를 담을 수 있는 크기의 결과 리스트 초기화
result = [0] * (n + m)
i = 0
j = 0
k = 0

# 모든 원소과 결과 리스트에 담길 때 까지 반복
while i < n or j < m:
    # 리스트 B의 모든 원소가 처리되었거나, 리스트 A의 원소가 더 작을 때
    if j >= m or (i < n and a[i] <= b[j]):
        # 리스트 A의 원소를 결과 리스트로 옮기기
        result[k] = a[i]
        i += 1
    # 리스트 A의 모든 원소가 처리되었거나, 리스트 B의 원소가 더 작을 때
    else:
        # 리스트 B의 원소를 결과 리스트로 옮기기
        result[k] = b[j]
        j += 1
    k += 1

# 결과 리스트 출력
for i in result:
    print(i,end=' ')
