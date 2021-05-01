'''
시간초과 O(n^2)
n = int(input())
input_num = list(map(int,input().split()))
num = []
for i in range(n-1):
    for j in range(i + 1,n):
        if input_num[i] < input_num[j]:
            num.append(input_num[j])
            break
        else:
            continue
    if len(num) == i:
        num.append(-1)
num.append(-1)
print(*num)
'''

n = int(input())
input_num = list(map(int, input().split()))
result = [-1] * n
stack = []
for i in range(n):
    while len(stack) != 0 and input_num[stack[-1]] < input_num[i]:
        result[stack.pop()] = input_num[i]
    stack.append(i)
print(*result)