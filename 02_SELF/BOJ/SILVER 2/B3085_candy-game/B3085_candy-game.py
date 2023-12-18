# 소요시간 40분 pypy 476ms
import sys

sys.stdin = open('input.txt')


def check(ci, cj, ni, nj):
    copied = [x[:] for x in arr]
    copied[ci][cj], copied[ni][nj] = copied[ni][nj], copied[ci][cj]
    mmax = 0
    for ii in range(N):
        idx = 0
        now = copied[ii][0]
        cnt = 0
        while idx < N:
            if copied[ii][idx] == now: cnt += 1
            else:
                # print(ii, now, cnt)
                if mmax < cnt: mmax = cnt
                cnt = 1
                now = copied[ii][idx]
            idx += 1
        if mmax < cnt: mmax = cnt
    # print('열')
    # for c in copied:
    #     print(c)
    # print()
    for jj in range(N):
        idx = 0
        now = copied[idx][jj]
        cnt = 0
        while idx < N:
            if copied[idx][jj] == now: cnt += 1
            else:
                # print(jj, now, cnt)
                if mmax < cnt: mmax = cnt
                cnt = 1
                now = copied[idx][jj]
            idx += 1
        if mmax < cnt: mmax = cnt
    return mmax


delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# for _ in range(3):
N = int(input())
arr = [list(input()) for _ in range(N)]

answer = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        for di, dj in delta:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[i][j] == arr[ni][nj]: continue
            if visited[ni][nj]: continue
            v = check(i, j, ni, nj)
            if answer < v:
                answer = v
        visited[i][j] = 1
print(answer)