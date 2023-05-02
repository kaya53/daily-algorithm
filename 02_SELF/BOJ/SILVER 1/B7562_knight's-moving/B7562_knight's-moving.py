# 230502 pypy 320ms python 1076ms
import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs(si, sj, ei, ej):
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1

    move = -1
    while q:
        move += 1
        for _ in range(len(q)):
            ci, cj = q.popleft()
            if (ci, cj) == (ei, ej): return move
            for di, dj in delta:
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]: continue
                q.append((ni, nj))
                visited[ni][nj] = 1


delta = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
T = int(input())
for _ in range(T):
    N = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    print(bfs(si, sj, ei, ej))
