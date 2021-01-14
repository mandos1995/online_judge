"""
문제
두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
"""
num1, num2 = map(int, input().split())
if num1 > num2:
    print('>')
elif num1 == num2:
    print('==')
else:
    print('<')