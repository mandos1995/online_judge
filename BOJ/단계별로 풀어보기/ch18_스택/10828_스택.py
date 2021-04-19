import sys
input = sys.stdin.readline

stack = []
cmd = []
N = int(input())
for i in range(N):
    cmd = input().strip().split()
    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    if cmd[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    if cmd[0] == 'size':
        print(len(stack))
    if cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if cmd[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])