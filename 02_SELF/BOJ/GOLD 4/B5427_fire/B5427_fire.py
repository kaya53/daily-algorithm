# 소요시간 30분 pypy 724ms
import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs(move, fire, board, n, m):
    time = 0
    cnt = len(fire)
    visited = [[0]*m for _ in range(n)]
    while cnt < n*m and move:
        time += 1
        # print(time, '-----------')
        # print('fire', fire)
        while fire:
            for _ in range(len(fire)):
                fi, fj = fire.popleft()

                for di, dj in delta:
                    nfi, nfj = fi+di, fj+dj
                    if nfi < 0 or nfi >= n or nfj < 0 or nfj >=m: continue
                    if board[nfi][nfj] == '#' or board[nfi][nfj] == '*': continue
                    board[nfi][nfj] = '*'
                    fire.append((nfi, nfj))
            break
        # print('move', move)
        while move:
            for _ in range(len(move)):
                ci, cj = move.popleft()

                if ci == 0 or ci == n-1 or cj == 0 or cj == m-1:
                    return time

                for di, dj in delta:
                    ni, nj = ci + di, cj + dj
                    if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
                    if visited[ni][nj] or board[ni][nj] == '#' or board[ni][nj] == '*': continue
                    visited[ni][nj] = 1
                    move.append((ni, nj))
            break
    return 'IMPOSSIBLE'


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solution(n, m,board):
    fire = deque()
    si, sj = -1, -1
    for i in range(n):
        for j in range(m):
            if board[i][j] == '*': fire.append((i, j))
            elif board[i][j] == '@': si, sj = i, j
    r = bfs(deque([(si, sj)]), fire, board, n, m)
    print(r)


T = int(input())
for _ in range(T):
    W, H = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    solution(H, W, arr)