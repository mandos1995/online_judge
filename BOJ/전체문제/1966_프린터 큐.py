t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = list(map(int,input().split()))
    index = list(range(len(queue)))
    index[m] = 'target'
    count = 0

    while True:
        if queue[0] == max(queue):
            count += 1
            if index[0] == 'target':
                print(count)
                break
            else:
                queue.pop(0)
                index.pop(0)
        else:
            queue.append(queue.pop(0))
            index.append(index.pop(0))