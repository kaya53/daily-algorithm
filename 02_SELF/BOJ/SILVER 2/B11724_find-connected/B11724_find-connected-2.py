import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        now = q.popleft()
        for nnext in adj[now]:
            if visited[nnext]: continue
            q.append(nnext)
            visited[nnext] = 1


N, M = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(M):
    s, e = map(lambda x: int(x)-1, input().split())
    adj[s].append(e)
    adj[e].append(s)

visited = [0] * N
res = 0
for i in range(N):
    if visited[i]: continue
    bfs(i)
    res += 1
print(res)
