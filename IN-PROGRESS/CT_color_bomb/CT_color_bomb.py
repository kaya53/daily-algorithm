import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs(si, sj, color):
    q = deque([(si, sj)])
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1
    whole = 1
    red_cnt = 0
    std_i, std_j = si, sj

    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]: continue
            if arr[ni][nj] < 0 or (arr[ni][nj] >= 1 and arr[ni][nj] != color): continue
            whole += 1
            q.append((ni, nj))
            visited[ni][nj] = 1

            if not arr[ni][nj]: red_cnt += 1
            elif arr[ni][nj] > 0:
                if std_i < ni:
                    std_i, std_j = ni, nj
                elif std_i == ni and std_j > nj:
                    std_j = nj
    return whole, red_cnt, std_i, std_j


def hit_bombs(si, sj, color):
    cnt = 0
    q = deque([(si, sj)])
    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
            if arr[ni][nj] < 0 or (arr[ni][nj] >= 1 and arr[ni][nj] != color): continue
            cnt += 1
            arr[ni][nj] = -2  # 터진 폭탄 표시
            q.append((ni, nj))
    return cnt


def gravity(arr):
    for jj in range(N):
        nums = []
        empty = []
        new = []
        for ii in range(N):
            if arr[ii][jj] == -1:
                new += empty + nums + [-1]
                empty = []
                nums = []
            elif arr[ii][jj] == -2:
                empty.append(-2)
            else:
                nums.append(arr[ii][jj])
        new += empty + nums
        # print(new)
        for pi in range(N):
            arr[pi][jj] = new[pi]


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

score = 0
while True:
    # 1. 터뜨릴 폭탄 묶음 찾기
    candidates = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                w, r, sti, stj = bfs(i, j, arr[i][j])
                if w > 1: candidates.append((w, r, sti, stj))
    if not candidates: break
    candidates.sort(key=lambda x:[x[0], -x[1], x[2], -x[3]])
    bombed = candidates.pop()
    # print(bombed)

    # 2. 폭탄 터뜨리기
    res = hit_bombs(bombed[2], bombed[3], arr[bombed[2]][bombed[3]])
    score += res*res

    # 3. 중력 작용 => 전치해서 하고 다시 되돌려 놓기
    # for a in arr:
    #     print(a)
    # print()
    gravity(arr)
    # for a in arr:
    #     print(a)
    # print()
    arr = list(map(list, zip(*arr)))[::-1]
    # for a in arr:
    #     print(a)
    # print()
    gravity(arr)
    # for a in arr:
    #     print(a)
    # print()
    # break
print(score)

