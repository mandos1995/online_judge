from collections import deque
queue = deque()
out = []
n, k = map(int, input().split())
for i in range(1, n + 1):
    queue.append(i)
while len(queue) > 0:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    out.append(queue.popleft())

out = str(out).replace('[','<').replace(']','>')
print(out)