'''
문제
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
예를 들어, 서로 다른 9개의 자연수
3, 29, 38, 12, 57, 74, 40, 85, 61
이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
'''

# solution
list_num = []
for i in range(9):
    list_num.append(input())
max = list_num[0]
for i in range(len(list_num)):
    if max < list_num[i]:
        max = list_num[i]
        index = i + 1
print(max)
print(index)

# 더 쉬운 solution
num = []
for i in range(9):
    num.append(int(input()))
print(max(num))
print(num.index(max(num))+1)
    