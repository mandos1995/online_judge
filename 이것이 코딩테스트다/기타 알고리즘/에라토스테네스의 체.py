# 에라토스테네스의 체 알고리즘은 여러 개의 수가 소수인지 아닌지를 판별할 때 사용하는 대표적인 알고리즘
# 에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾을 때 사용할 수 있다.

# 1. 2 부터 N까지의 모든 자연수를 나열
# 2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
# 3. 남은 수 중에서 i의 배수를 모두 제거한다. (i는 제거 안함)
# 4. 더 이상 반복할 수 없을 때 까지 2번 3번 과정 반복

# 시간복잡도 O(NloglogN)
import math

n = 1000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)] # 처음엔 모든 소수(True)인 것으로 초기화 (0과 1은 제외)

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하여
    if array[i] == True: # i가 소수인 경우 (남은 수 인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')

