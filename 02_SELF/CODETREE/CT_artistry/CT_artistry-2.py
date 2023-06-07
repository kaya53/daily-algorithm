# 230607 python 1475ms => 1시간 ~ 1시간 30분 소요

import sys

sys.stdin = open('input.txt')

from collections import deque


def ff(si, sj, num, new_num, g_arr):
    q = deque([(si, sj)])
    visited[si][sj] = 1
    cnt = 1
    g_arr[si][sj] = new_num

    while q:
        ci, cj = q.popleft()

        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]: continue
            if arr[ni][nj] != num: continue
            g_arr[ni][nj] = new_num
            q.append((ni, nj))
            cnt += 1
            visited[ni][nj] = 1
    return cnt, g_arr


def get_adj_cnt(si, sj, g1_num, g2_num, g_arr):
    # 전역의 visited 초기화해서 사용
    for ii in range(N):
        for jj in range(N):
            visited[ii][jj] = 0
    q = deque([(si, sj)])
    visited[si][sj] = 1
    cnt = 0  # 인접한 변의 개수

    while q:
        ci, cj = q.popleft()

        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]: continue
            if g_arr[ni][nj] == g2_num: cnt += 1
            if g_arr[ni][nj] != g1_num: continue
            q.append((ni, nj))
            visited[ni][nj] = 1
    return cnt


def rotate():
    global arr

    new = [[0] * N for _ in range(N)]
    # 십자 모양 반시계 회전
    for i in range(half):
        new[i][half], new[half][N-1-i], new[N-1-i][half], new[half][i] = arr[half][N-1-i], arr[N-1-i][half], arr[half][i], arr[i][half]
    new[half][half] = arr[half][half]
    # 격자 시계 회전
    for si, sj in [(0, 0), (0, half+1), (half+1, 0), (half+1, half+1)]:
        for ki in range(half):
            for kj in range(half):
                new[si+kj][sj+half-ki-1] = arr[si+ki][sj+kj]
    # for n in new:
    #     print(n)
    arr = new


def solve():
    g_arr = [[0] * N for _ in range(N)]
    groups = []
    new_num = 1
    # 전역의 visited 초기화해서 사용
    for ii in range(N):
        for jj in range(N):
            visited[ii][jj] = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                now_cnt, g_arr = ff(i, j, arr[i][j], new_num, g_arr)
                groups.append((i, j, now_cnt, arr[i][j], new_num))
                new_num += 1

    now_score = 0
    lenG = len(groups)
    for gr1 in range(lenG):
        for gr2 in range(gr1 + 1, lenG):
            gi1, gj1, gcnt1, init_no1, grp_no1 = groups[gr1]
            gi2, gj2, gcnt2, init_no2, grp_no2 = groups[gr2]
            adj_cnt = get_adj_cnt(gi1, gj1, grp_no1, grp_no2, g_arr)
            now_score += (gcnt1 + gcnt2) * init_no1 * init_no2 * adj_cnt
            # now_score += now
            # print(gr1, gr2, now)
            # print([gcnt1, gcnt2, init_no1, init_no2, adj_cnt])
    # print(now_score)
    rotate()

    return now_score


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# for _ in range(2):
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
half = N//2
visited = [[0] * N for _ in range(N)]

score = 0
for _ in range(4):
    score += solve()

print(score)