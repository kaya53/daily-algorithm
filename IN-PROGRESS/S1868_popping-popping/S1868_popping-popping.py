# 230526 pypy 734ms => 1시간 ~ 1시간 30분 소요
import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs(si, sj):
    global zero_cnt, other_cnt

    q = deque([(si, sj)])
    visited[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]: continue
            if bomb[ni][nj] == 0:
                zero_cnt -= 1
                q.append((ni, nj))
                visited[ni][nj] = 1
            else:
                other_cnt -= 1
                visited[ni][nj] = 1


def count_bomb():
    b_arr = [[0] * N for _ in range(N)]
    # cnt = 0
    # 주변에 지뢰가 몇개나 있는 지 찾기, 지뢰없는 칸 세기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '*':
                b_arr[i][j] = -1
            else:
                for di, dj in delta:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
                    if arr[ni][nj] == '*': b_arr[i][j] += 1
    return b_arr


def count_zero_other():
    z_cnt = 0
    o_cnt = 0
    for r in range(N):
        for c in range(N):
            if bomb[r][c] == 0:
                z_cnt += 1
            elif bomb[r][c] > 0:
                o_cnt += 1
    return z_cnt, o_cnt


def solve():
    global zero_cnt

    res = 0
    for bi in range(N):
        for bj in range(N):
            if visited[bi][bj]: continue
            if bomb[bi][bj] == 0:
                zero_cnt -= 1
                bfs(bi, bj)
                res += 1
            if not zero_cnt: return res + other_cnt


delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]

    bomb = count_bomb()
    zero_cnt, other_cnt = count_zero_other()
    visited = [[0] * N for _ in range(N)]

    print(f'#{tc} {solve()}')

