import sys

sys.stdin = open('input.txt')

from collections import deque

n, m = map(int, input().split())  # 행, 열의 길이; 1, 1부터 시작
r, c, s, k = map(int, input().split())  # 말의 위치, 졸의 위치
board = [[0] * m for _ in range(n)]  # 장기판

dir_ls = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
# 말에서 시작해 bfs
res = 0
q = deque()
q.append((r-1, c-1, 0))  # 말의 시작 위치, 이동 횟수
while q:
    mi, mj, move_cnt = q.popleft()
    if mi == s-1 and mj == k-1:
        res = move_cnt
        break

    for di, dj in dir_ls:
        ni, nj = mi + di, mj + dj
        if ni < 0 or ni >= n or nj < 0 or nj >= m or (ni == r-1 and nj == c-1): continue
        if not board[ni][nj]: # 방문 안한 점
            board[ni][nj] = move_cnt + 1
            q.append((ni, nj, move_cnt + 1))

print(res)
