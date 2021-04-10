# 비효율적인 소수 판별 알고리즘
# 2 부터 X - 1 까지의 모든 자연수로 나누었을때 나누어 떨어지는 수가 하나라도 있으면 소수 아님

# 소수 판별 함수 - 시간복잡도 O(x)
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False # 소수 아님

        return True # 소수임

# 모든 자연수로 나눈다는 것은 비효율적이기 때문에 제곱근 까지만(가운데 약수) 확인하는 알고리즘
import math

# 소수 판별 알고리즘 - 시간복잡도 O(x^1/2)
def is_prime_number2(x):
    # 2부터 x의 제곱근 까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x) + 1)):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False  # 소수 아님

        return True  # 소수임