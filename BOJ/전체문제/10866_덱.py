from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
deque = deque()

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push_front':
        deque.appendleft(int(cmd[1]))
    if cmd[0] == 'push_back':
        deque.append(int(cmd[1]))
    if cmd[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())
    if cmd[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    if cmd[0] == 'size':
        print(len(deque))
    if cmd[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    if cmd[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    if cmd[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])