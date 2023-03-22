import sys

sys.stdin = open('input.txt')

from collections import deque

# for _ in range(3):
n, m, v = map(int, input().rstrip().split())
infos = [list(map(int, input().rstrip().split())) for _ in range(m)]

adj = [[] for _ in range(n+1)]
for s, e in infos:
    adj[s].append(e)
    adj[e].append(s)

for x in range(1, n+1):
    adj[x] = sorted(adj[x])

visited = [False] * (n+1)

def dfs(v, cnt):
    if visited[v]:
        return
    visited[v] = True
    print(v, end=' ')
    for nv in adj[v]:
        dfs(nv, cnt+1)

dfs(v, 0)
print()

q = deque()
q.append(v)
visited2 = [False] * (n+1)

def bfs():
    while q:
        now_v = q.popleft()
        if not visited2[now_v]:
            visited2[now_v] = True
            print(now_v, end=' ')
            for nv in adj[now_v]:
                q.append(nv)

bfs()
print()
