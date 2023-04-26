import sys
sys.stdin = open('input.txt')

from collections import deque

N = int(input())
V = int(input())

adj = [[] for _ in range(N+1)]
for _ in range(V):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

visited = [0] * (N+1)
q = deque()
q.append(1)
visited[1] = 1
cnt = 0
while q:
    now = q.popleft()
    for nnext in adj[now]:
        if visited[nnext]: continue
        q.append(nnext)
        visited[nnext] = 1
        cnt += 1
print(cnt)