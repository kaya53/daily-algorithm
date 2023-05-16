import sys

sys.stdin = open('input.txt')

from collections import deque

def bfs(ci, cj, color):
    q = deque()
    q.append((ci, cj))
    visited[ci][cj] = 1
    cnt = 1

    while q:
        ci, cj = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M or visited[ni][nj] or arr[ni][nj] != color: continue
            q.append((ni, nj))
            visited[ni][nj] = 1
            cnt += 1

    return cnt**2


M, N = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
our = 0
enemy = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]: continue
        if arr[i][j] == 'W':
            our += bfs(i, j, 'W')
        else:
            enemy += bfs(i, j, 'B')

print(our, enemy)