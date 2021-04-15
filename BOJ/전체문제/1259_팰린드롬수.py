while True:
    num = input()
    if num == '0':
        break
    if num[0] == '0':
        print('no')
    elif num == num[::-1]:
        print('yes')
    else:
        print('no')