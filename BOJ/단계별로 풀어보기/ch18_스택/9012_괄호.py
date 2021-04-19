n = int(input())
stack = []
for _ in range(n):
    ps = input()
    if ps[0] == ')':
        print('NO')
    else:
        for i in ps:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if len(stack) == 0:
                    stack.append(i)
                else:
                    if stack[-1] == '(':
                        stack.pop()
            else:
                continue
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')

        stack.clear()
