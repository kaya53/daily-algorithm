import sys
from collections import deque

input = sys.stdin.readline
# sys.stdin = open('input.txt')


def bfs(q):
    while q:
        now = q.popleft()
        res.append(now)

        for nnext in adj[now]:
            in_degree[nnext] -= 1
            if not in_degree[nnext]: q.append(nnext)


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    in_degree[e] += 1

res = []
bfs(deque([i for i in range(1, N+1) if not in_degree[i]]))

print(" ".join(map(str, res)))