'''
문제
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

# solution
import sys
T = int(sys.stdin.readline().rstrip())
for i in range(1,T+1):
    print(i)