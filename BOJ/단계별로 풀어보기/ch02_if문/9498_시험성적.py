'''
문제
시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
'''

# solution
# 파이썬에는 switch 문이 없으므로 if 문을 사용
score = int(input())
score = int(score / 10)
if score == 9 or score == 10:
    print('A')
elif score == 8:
    print('B')
elif score == 7:
    print('C')
elif score == 6:
    print('D')
else:
    print('F')