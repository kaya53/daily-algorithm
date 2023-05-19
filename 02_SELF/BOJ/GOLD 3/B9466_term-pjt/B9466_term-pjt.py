import sys
from collections import deque
# sys.stdin = open('input.txt')


def bfs(q):
    global cnt

    while q:
        now = q.popleft()
        cnt += 1

        nnext = adj[now]
        in_degree[nnext] -= 1
        if not in_degree[nnext]: q.append(nnext)


T = int(input())
for _ in range(T):
    N = int(input())
    adj = list(map(lambda x: int(x)-1, input().split()))
    in_degree = [0] * N
    for i in range(N):
        in_degree[adj[i]] += 1

    cnt = 0
    bfs(deque([i for i in range(N) if not in_degree[i]]))
    print(cnt)