import sys
n = int(input())
s = set([])
for _ in range(n):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == 'add':
        s.add(int(cmd[1]))
    elif cmd[0] == 'check':
        if int(cmd[1]) in s:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'remove':
        s.discard(int(cmd[1]))
    elif cmd[0] == 'toggle':
        if int(cmd[1]) in s:
            s.discard(int(cmd[1]))
        else:
            s.add(int(cmd[1]))
    elif cmd[0] == 'all':
        s = set(range(1, 21))
    elif cmd[0] == 'empty':
        s = set()
