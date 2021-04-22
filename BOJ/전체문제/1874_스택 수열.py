stack = []
result = []
n = int(input())
count = 0

for _ in range(n):
    num = int(input())
    while num > count:
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        result.append('NO')

if 'NO' in result:
    print('NO')
else:
    for i in range(len(result)):
        print(result[i])
