import sys
sys.stdin = open('input.txt')

from collections import deque


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M or not arr[ni][nj] or visited[ni][nj]: continue
            visited[ni][nj] = 1
            q.append((ni, nj))


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        arr[r][c] = 1

    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)