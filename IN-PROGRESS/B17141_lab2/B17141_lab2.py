# python 416ms
# 조합 + bfs
import sys

sys.stdin = open('input.txt')

from collections import deque


def check_time(choice, n, board):
    q = deque(choice)
    visited = [[-1] * n for _ in range(n)]
    for i, j in choice:
        visited[i][j] = 0
    time = 0

    while q:
        time += 1
        for _ in range(len(q)):
            ci, cj = q.popleft()

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = ci+di, cj+dj
                if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
                if board[ni][nj] == 1 or visited[ni][nj] > -1: continue
                visited[ni][nj] = time
                q.append((ni, nj))
    # 빈칸 체크 => 빈칸 있으면 시간 갱신 안함 n*n 반환
    for r in range(n):
        for c in range(n):
            # 바이러스가 갈 수 있는 곳인데 방문 안함
            if board[r][c] != 1 and visited[r][c] == -1: return n*n
    return time-1


def comb(depth, ci, k, n, m, candidate, choice, board):
    global answer

    if depth == m:
        # print(choice)
        now = check_time(choice, n, board)
        # print(choice, now)
        if answer > now:
            answer = now
        return

    for ni in range(ci+1, k):
        choice[depth] = candidate[ni]
        comb(depth+1, ni, k, n, m, candidate, choice, board)
        choice[depth] = ()


def solution(n, m, board):
    candidate = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                candidate.append((i, j))
    comb(0, -1, len(candidate), n, m, candidate, [() for _ in range(m)], board)


# for _ in range(7):
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = N*N
solution(N, M, arr)
if answer == N*N: print(-1)
else: print(answer)
