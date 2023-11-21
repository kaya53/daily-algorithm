import sys
from collections import deque


def bfs(s):
    global best

    q = deque([s])
    visited[s] = 1

    while q:
        now = q.popleft()
        now_w = weights[now]

        for other in graph[now]:
            if not visited[other]:
                q.append(other)
                visited[other] = 1
            if now_w <= weights[other]: break
        else:
            best += 1


N, M = map(int, input().split())
weights = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]  # 1번부터 시작하니까
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)
best = 0
for i in range(1, N + 1):
    if visited[i]: continue
    if graph[i]:
        bfs(i)
    else:
        best += 1
        visited[i] = 1
print(best)