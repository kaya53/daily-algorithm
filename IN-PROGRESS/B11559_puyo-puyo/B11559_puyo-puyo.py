# 소요시간 40분: python 68ms
# 단순한 ff, 중력 문제

import sys

sys.stdin = open('input.txt')

from collections import deque


def bomb(arr):
    res = []
    visited = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j] == '.' or visited[i][j]: continue
            color = arr[i][j]
            # print(i, j)
            q = deque([(i, j)])
            ls = [(i, j)]
            visited[i][j] = 1
            while q:
                ci, cj = q.popleft()
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = ci + di, cj + dj
                    if ni < 0 or ni >= 12 or nj < 0 or nj >= 6: continue
                    if arr[ni][nj] != color or visited[ni][nj]: continue
                    q.append((ni, nj))
                    ls.append((ni, nj))
                    visited[ni][nj] = 1
            if len(ls) >= 4: res.append(ls)
    return res


def gravity(arr):
    for j in range(6):
        stack = []
        for i in range(12):
            if arr[i][j] != '.':
                stack.append(arr[i][j])
        stack = ['.']*(12-len(stack)) + stack
        # print(stack)
        for ii in range(12):
            arr[ii][j] = stack[ii]
    return arr


def solution():
    arr = [list(input()) for _ in range(12)]

    cnt = 0
    while True:
        bomb_ls = bomb(arr)
        if not bomb_ls: return cnt
        cnt += 1
        for bls in bomb_ls:
            for bi, bj in bls:
                arr[bi][bj] = '.'

        arr = gravity(arr)


print(solution())

