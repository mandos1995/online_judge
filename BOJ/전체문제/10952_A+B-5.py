'''
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력의 마지막에는 0 두개가 들어옴
'''

# solution
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        print(A+B)