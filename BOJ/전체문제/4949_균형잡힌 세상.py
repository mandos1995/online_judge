string = ''
stack = []
while True:
    string = input()
    if string == '.':
        break
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        if i == ']' or i == ')':
            if len(stack) == 0:
                stack.append(i)
            if len(stack) > 0:
                if (stack[-1] == '[' and i == ')') or (stack[-1] == '(' and i == ']'):
                    stack.append(i)
        if len(stack) > 0:
            if (stack[-1] == '[' and i == ']') or (stack[-1] == '(' and i == ')'):
                stack.pop()
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
    stack.clear()
