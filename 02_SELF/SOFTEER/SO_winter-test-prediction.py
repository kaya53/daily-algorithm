# 전형적 bfs, Floyd-Fill 문제 => 치즈나 빙하 문제와 유사

import sys
from collections import deque


def get_air(arr):
    for i in range(N):
        for j in range(M):
            if not arr[i][j]:
                q = deque([(i, j)])
                visited = [[0] * M for _ in range(N)]
                visited[i][j] = 1
                air = {(i, j)}
                while q:
                    ci, cj = q.popleft()
                    for di, dj in delta:
                        ni, nj = ci + di, cj + dj
                        if ni < 0 or ni >= N or nj < 0 or nj >= M or visited[ni][nj] or arr[ni][nj]: continue
                        q.append((ni, nj))
                        visited[ni][nj] = 1
                        air.add((ni, nj))
                return air


def melting(air, arr):
    visited = [[0] * M for _ in range(N)]
    melted = []
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j]:
                q = deque([(i, j)])
                visited[i][j] = 1
                while q:
                    ci, cj = q.popleft()
                    cnt = 0
                    for di, dj in delta:
                        ni, nj = ci + di, cj + dj
                        if ni < 0 or ni >= N or nj < 0 or nj >= M: continue
                        if (ni, nj) in air:
                            cnt += 1
                        elif arr[ni][nj] and not visited[ni][nj]:
                            q.append((ni, nj))
                            visited[ni][nj] = 1
                    if cnt >= 2: melted.append((ci, cj))
    return melted


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
arr = [[] for _ in range(N)]
ice = 0
for k in range(N):
    inp = list(map(int, input().split()))
    arr[k] = inp
    for v in inp:
        if v: ice += 1

time = 0
while ice:
    time += 1
    air = get_air(arr)
    # print(air)
    # break
    melted = melting(air, arr)

    for mi, mj in melted:
        arr[mi][mj] = 0
        ice -= 1

print(time)