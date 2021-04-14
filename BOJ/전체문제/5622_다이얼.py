'''
문제
상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.
전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 
숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
숫자 1을 걸려면 총 2초가 필요하다. 
1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 
즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.
'''

# solution
dials = input()
dials = dials.upper()
dials_sum = 0
for dial in dials:
  if dial in 'ABC':
    dials_sum = dials_sum + 3
  if dial in 'DEF':
    dials_sum = dials_sum + 4
  if dial in 'GHI':
    dials_sum = dials_sum + 5
  if dial in 'JKL':
    dials_sum = dials_sum + 6
  if dial in 'MNO':
    dials_sum = dials_sum + 7
  if dial in 'PQRS':
    dials_sum = dials_sum + 8
  if dial in 'TUV':
    dials_sum = dials_sum + 9
  if dial in 'WXYZ':
    dials_sum = dials_sum + 10
print(dials_sum)