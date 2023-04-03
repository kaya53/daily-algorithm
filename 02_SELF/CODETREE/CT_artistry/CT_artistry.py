import sys
from collections import deque
sys.stdin = open('input.txt')


def ff(si, sj, visited, group_no, num):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = group_no
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n or visited[ni][nj]: continue
            if arr[ni][nj] != num: continue
            visited[ni][nj] = group_no
            q.append((ni, nj))
            cnt += 1
    return cnt, visited


def find_group():
    visited = [[0] * n for _ in range(n)]
    group_no = 1
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt, visited = ff(i, j, visited, group_no, arr[i][j])
                group_no += 1
                group.append((i, j, arr[i][j], cnt))  # 전역 변수 group
    return visited


def comb(len_group):
    res = []
    for i in range(1, len_group):
        for j in range(i+1, len_group):
            res.append((i, j))
    # print(res)
    return res


def calc_harmony(comb_ls, visited):
    global score

    harmony = [] * len(comb_ls)
    for g1, g2 in comb_ls:
        checked = [[0] * n for _ in range(n)]
        si, sj = group[g1][0], group[g1][1]
        q = deque()
        q.append((si, sj))
        checked[si][sj] = 1
        adj_cnt = 0
        while q:
            ci, cj = q.popleft()
            for di, dj in delta:
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= n or nj < 0 or nj >= n or checked[ni][nj]: continue
                if visited[ni][nj] == g2:
                    adj_cnt += 1
                    continue
                elif visited[ni][nj] == g1:
                    q.append((ni, nj))
                    checked[ni][nj] = 1
        if adj_cnt:
            g1_num, g1_cnt = group[g1][2:]
            g2_num, g2_cnt = group[g2][2:]
            now_sc = (g1_cnt + g2_cnt) * g1_num * g2_num * adj_cnt
            score += now_sc


def rotate(arr):
    rotated = [[0] * n for _ in range(n)]
    # 십자를 반시계로
    half = n//2
    for k in range(half):
        rotated[k][half], rotated[half][k], rotated[n-k-1][half], rotated[half][n-k-1] = \
            arr[half][n-k-1], arr[k][half], arr[half][k], arr[n-k-1][half]
    rotated[half][half] = arr[half][half]

    # 격자 시계 90도 회전
    for i in range(0, n, half+1):
        for j in range(0, n, half+1):
            for ki in range(half):
                for kj in range(half):
                    rotated[i+kj][j+half-ki-1] = arr[i+ki][j+kj]
    return rotated
    

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# for _ in range(2):
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

score = 0
for _ in range(4):
    group = [0]  # 매 턴마다 갱신되어야 함
    visited = find_group()
    # print(group)
    calc_harmony(comb(len(group)), visited)
    arr = rotate(arr)
print(score)
