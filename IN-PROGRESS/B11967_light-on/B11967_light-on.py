import sys

# sys.stdin = open('input.txt')

from collections import deque


def bfs():
    global mmax

    if info.get((0, 0), -1) == -1: return

    visited[0][0] = 0
    arr[0][0] = 1
    q = deque()
    q.append((0, 0, 1))

    dist = 0
    while q:
        dist += 1
        for _ in range(len(q)):
            ci, cj, cnt = q.popleft()
            
            # 불 켜기
            if info.get((ci, cj), -1) != -1:
                ti, tj = -1, -1
                for ii, jj in info[(ci, cj)]:
                    if arr[ii][jj]: continue
                    arr[ii][jj] = 1
                    cnt += 1
                    if -1 < visited[ii][jj] < dist:
                        ti, tj = ii, jj
                if ti > -1 and tj > -1:
                    q.append((ti, tj, cnt))

            if mmax < cnt: mmax = cnt

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
                if visited[ni][nj] == -1: visited[ni][nj] = dist
                if not arr[ni][nj]: continue

                if visited[ni][nj] == dist:
                    q.append((ni, nj, cnt))


# for _ in range(3):
N, M = map(int, input().split())
info = {}
for _ in range(M):
    si, sj, ei, ej = map(lambda x:int(x)-1, input().split())
    if info.get((si, sj), -1) == -1:
        info[(si, sj)] = set()
    info[(si, sj)].add((ei, ej))


visited = [[-1]*N for _ in range(N)]
arr = [[0]*N for _ in range(N)]
mmax = 1
bfs()

print(mmax)
