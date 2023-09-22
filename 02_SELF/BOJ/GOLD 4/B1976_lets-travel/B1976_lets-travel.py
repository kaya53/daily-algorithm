# 소요시간 30분 python 264ms, pypy 236ms
# bfs로 visited를 하되 한 번만 해서 visited 배열을 만들어놓고
# 그걸 이용해서 각 경로가 가능한 지 보면 됨

import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque


def bfs(start):
    q = deque([(start, 0)])
    visited = [-1] * N
    visited[start] = 0

    while q:
        curr, dist = q.popleft()
        nnext = adj[curr]
        for k in range(N):
            if not nnext[k] or visited[k] > -1: continue
            q.append((k, dist+1))
            visited[k] = dist + 1
    return visited


N = int(input().rstrip())
M = int(input().rstrip())
adj = [list(map(int, input().rstrip().split())) for _ in range(N)]
path = list(map(lambda x: int(x)-1, input().rstrip().split()))

res = [[] for _ in range(N)]
for z in range(N):
    res[z] = bfs(z)

ans = 'YES'
for i in range(M-1):
    s, e = path[i], path[i+1]
    if res[s][e] == -1:  # 경로 없음
        ans = 'NO'
        break
print(ans)