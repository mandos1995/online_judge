n = int(input())
cmd = []
for _ in range(n):
    cmd.append(input())

length = len(cmd[0])
new_cmd = list(cmd[0])
for i in range(n):
    for j in range(length):
        if new_cmd[j] == cmd[i][j]:
            continue
        else:
            new_cmd[j] = '?'
print(''.join(new_cmd))