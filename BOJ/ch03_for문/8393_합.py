'''
문제
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
'''

# solution
N = int(input())
sum = 0
for i in range(1,N+1):
    sum += i
print(sum)