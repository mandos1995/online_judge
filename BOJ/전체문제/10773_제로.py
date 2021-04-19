n = int(input())
stack = []
for _ in range(n):
    stack_element = int(input())
    if stack_element == 0:
        stack.pop()
    else:
        stack.append(stack_element)
print(sum(stack))