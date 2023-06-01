# 230601 python 234ms => 1시간 소요
# 정렬을 잘하면 되는 문제
import sys

sys.stdin = open('input.txt')


def solve(s_no, fav_ls):
    # print(s_no, fav_ls)
    can_sit = []
    for i in range(N):
        for j in range(N):
            like, empty = 0, 0
            for di, dj in delta:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
                if not arr[ni][nj]: empty += 1
                elif arr[ni][nj] and arr[ni][nj] in fav_ls: like += 1
                if not arr[i][j]:
                    can_sit.append((like, empty, i, j))
    can_sit.sort(key=lambda x: [-x[0], -x[1], x[2], x[3]])
    # print(can_sit)
    like, empty, ci, cj = can_sit.pop(0)
    arr[ci][cj] = s_no


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# for _ in range(2):
N = int(input())
arr = [[0] * N for _ in range(N)]
info = {}
for _ in range(N**2):
    s, *fav = map(int, input().split())
    info[s] = fav
    solve(s, fav)

score = 0
# output
for i in range(N):
    for j in range(N):
        like_cnt = -1
        for di, dj in delta:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
            if arr[ni][nj] in info[arr[i][j]]: like_cnt += 1
        # print(i, j, like_cnt)
        score += int(10**like_cnt)
print(score)