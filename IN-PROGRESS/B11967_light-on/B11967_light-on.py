import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs():
    global mmax

    if info.get((0,0), -1) == -1: return 0
    cc = 1
    for r, c in info[(0, 0)]:
        arr[r][c] = 1
        cc += 1
    visited[0][0] = 1
    arr[0][0] = 1
    q = deque()
    q.append((0, 0, cc))

    while q:
        ci, cj, cnt = q.popleft()
        if mmax < cnt: mmax = cnt

        for di, dj in [(-1,0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]: continue
            if not arr[ni][nj]: continue

            if info.get((ni, nj), -1) != -1:
                num = len(info[(ni, nj)])
                for ii, jj in info[(ni, nj)]:
                    if arr[ii][jj]: continue
                    arr[ii][jj] = 1
                    if visited[ii][jj]: q.append((ii, jj, cnt+num))
                q.append((ni, nj, cnt+num))
            else:
                q.append((ni, nj, cnt))
            visited[ni][nj] = 1


N, M = map(int, input().split())
info = {}
for _ in range(M):
    si, sj, ei, ej = map(lambda x:int(x)-1, input().split())
    if info.get((si, sj), -1) == -1:
        info[(si, sj)] = set()
    info[(si, sj)].add((ei, ej))


visited = [[0]*N for _ in range(N)]
arr = [[0]*N for _ in range(N)]
mmax = 0
bfs()
print(mmax)
for a in arr:
    print(a)