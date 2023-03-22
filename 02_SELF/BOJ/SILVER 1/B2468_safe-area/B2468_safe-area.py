import sys

sys.stdin = open('input.txt')

from collections import deque


def get_safearea(rain, si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    while q:
        ci, cj = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n or arr[ni][nj] <= rain or visited[ni][nj]: continue
            visited[ni][nj] = 1
            q.append((ni, nj))


# for _ in range(3):
n = int(input())

arr = [[] for _ in range(n)]
# 최소 높이, 최대 높이
mmax = 0
for k in range(n):
    inp = list(map(int, input().split()))
    mmax = max(mmax, max(inp))
    arr[k] = inp

max_cnt = 0
# 물에 잠기는 지역이 없을 수도 있으니까 0부터 시작
for rain in range(mmax+1):
    visited = [[0] * n for _ in range(n)]
    turn_cnt = 0
    for ci in range(n):
        for cj in range(n):
            if arr[ci][cj] <= rain: continue  # 잠긴 지역 pass
            if visited[ci][cj]: continue
            get_safearea(rain, ci, cj)
            turn_cnt += 1
    # print(turn_cnt)
    if max_cnt < turn_cnt:
        max_cnt = turn_cnt
print(max_cnt)