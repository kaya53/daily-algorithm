import sys

sys.stdin = open('input.txt')

from collections import deque

n = int(input())
adj = [0] + [[] for _ in range(n)]

for _ in range(n-1):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

q = deque()
q.append(1)  # 시작점
visited = [0] * (n+1)
while q:
    now = q.popleft()

    for next_n in adj[now]:
        if not visited[next_n]:
            visited[next_n] = now
            q.append(next_n)

for k in range(2, n+1):
    print(visited[k])
