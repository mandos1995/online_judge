weather = int(input())
if weather == 12 or weather == 1 or weather == 2:
    print('winter')
elif weather//3 == 1:
    print('spring')
elif weather//3 == 2:
    print('summer')
elif weather//3 == 3:
    print('fall')
else:
    print('잘못입력하셨습니다. 1 ~ 12월 입력하세요.')