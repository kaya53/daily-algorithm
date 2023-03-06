import sys

sys.stdin = open('input.txt')

from itertools import permutations
from collections import deque

def bfs(s, e, visited):
    q = deque()
    q.append((s, 0))
    visited[s] = 1

    while q:
        now, click = q.popleft()
        print(now, click)
        if now == e:
            return click
        for nnext in adj[now]:
            if not visited[nnext]:
                q.append((nnext, click+1))


n = int(input())
adj = [[] for _ in range(n+1)]

# 인접 행렬
maxNode = 0
for x in range(1, n+1):
    s, e = map(int, input().split())
    adj[s].append(e)
    if maxNode < s:
        maxNode = s
    if maxNode < e:
        maxNode = e

ans = 0
cnt = 0  # 가능한 조합 수
for s, e in permutations(list(range(1, maxNode+1)), 2):
    # visited = [0] * (n+1)
    res = bfs(s, e, [0] * (n+1))
    if res:
        cnt += 1
        ans += res
print(f'{ans/cnt:.3f}')