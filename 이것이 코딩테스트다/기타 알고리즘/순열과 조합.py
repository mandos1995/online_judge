# 순열이란 서로 다른 n 개에서 r 개를 선택하여 일렬로 나열하는 것
# nPr 이라고 표현하며의, 경우의 수를 계산하는 공식은 nPr = n! / (n - r)!
# 모든 경우의 수를 다 출력하려면 itertools 라이브러리의 permutations 를 이용

# 1부터 4까지의 수 중에서 2개를 뽑아 한 줄로 새우는 모든 경우를 구하는 코드

import itertools

data = [1, 2, 3, 4]
print('순열')
for x in itertools.permutations(data, 2):
    print(list(x)) # 리스트 형태가 아니기 때문에 리스트로 바꿔줌

# 조합이란 서로 다른 n 개에서 순서에 상관없이 서로 다른 r 개를 선택하는것
# nCr 이라고 표현하며, 경우의 수를 계산하는 공식은 nCr = n! / r! * (n - r)!
# itertools 의 combinations() 함수 이용

import itertools

data = [1, 2, 3, 4]
print('조합')
for x in itertools.combinations(data, 2):
    print(list(x)) # 리스트 형태가 아니기 때문에 리스트로 바꿔줌



