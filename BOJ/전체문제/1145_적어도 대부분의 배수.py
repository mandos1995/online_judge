from itertools import combinations
from math import gcd
import sys

def solution(arr):
    def lcm(x, y):
        return x * y // gcd(x, y)
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]

num = list(map(int, input().split()))
min = sys.maxsize
for x in combinations(num, 3):
    if min > solution(list(x)):
        min = solution(list(x))
print(min)