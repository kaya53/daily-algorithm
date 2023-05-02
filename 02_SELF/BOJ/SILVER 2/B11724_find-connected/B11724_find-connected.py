import sys

sys.stdin = open('input.txt')

from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        now = q.popleft()
        for n in adj[now]:
            if visited[n]: continue
            q.append(n)
            visited[n] = 1


# for _ in range(2):
N, M = map(int, input().split())
visited = [0] * (N+1)
adj = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

cnt = 0
for i in range(1, N+1):
    if visited[i]: continue
    bfs(i)
    cnt += 1
print(cnt)

# cnt = 0
# for i in range(1, 1001, 2):
#     print(i, i+1)
#     cnt += 1
# print(cnt)