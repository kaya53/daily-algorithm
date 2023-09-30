# 소요시간 40분 pypy 336ms
# ff
import sys

sys.stdin = open('input.txt')

from collections import deque

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def find_air(arr, N, M):
    for i in range(N):
        for j in range(M):
            if not arr[i][j]:
                q = deque([(i, j)])
                visited = [[0] * M for _ in range(N)]
                visited[i][j] = 1

                while q:
                    ci, cj = q.popleft()
                    for di, dj in delta:
                        ni, nj = ci + di, cj + dj
                        if ni < 0 or ni >= N or nj < 0 or nj >= M: continue
                        if visited[ni][nj] or arr[ni][nj]: continue
                        q.append((ni, nj))
                        visited[ni][nj] = 1
                return visited


def find_cheeze(air_ls, arr, N, M):
    cnt = 0
    melt_ls = []
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = 1
                while q:
                    ci, cj = q.popleft()
                    air_adj = 0
                    for di, dj in delta:
                        ni, nj = ci + di, cj + dj
                        if ni < 0 or ni >= N or nj < 0 or nj >= M: continue
                        if air_ls[ni][nj] == 1: air_adj += 1
                        if visited[ni][nj] or not arr[ni][nj]: continue
                        q.append((ni, nj))
                        visited[ni][nj] = 1
                    if air_adj >= 2:
                        melt_ls.append((ci, cj))
                        cnt += 1
    return melt_ls, cnt

def solution():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    tot = 0
    for a in arr:
        tot += a.count(1)

    time = 0
    while tot > 0:
        time += 1
        air_ls = find_air(arr, N, M)
        melt_ls, melt_cnt = find_cheeze(air_ls, arr, N, M)
        # print(melt_ls)
        tot -= melt_cnt

        for mi, mj in melt_ls:
            arr[mi][mj] = 0

    return time

print(solution())