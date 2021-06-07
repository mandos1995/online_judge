from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n+1)]
visited = [False] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(1, n + 1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(1, n + 1):
            if not visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)


