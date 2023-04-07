import sys
from collections import deque
input = sys.stdin.readline


def bfs(si, sj):
    global res

    q = deque()
    q.append((si, sj, 0))
    path = [[0] * M for _ in range(N)]
    path[si][sj] = 1
    max_dist = 0

    while q:
        ci, cj, dist = q.popleft()
        if max_dist < dist:
            max_dist = dist
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M or arr[ni][nj] == 'W' or path[ni][nj]: continue
            path[ni][nj] = 1
            q.append((ni, nj, dist+1))

    if res < max_dist:
        res = max_dist


N, M = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
res = 0
for si in range(N):
    for sj in range(M):
        if arr[si][sj] == 'L' and not visited[si][sj]:
            visited[si][sj] = 1
            bfs(si, sj)
print(res)