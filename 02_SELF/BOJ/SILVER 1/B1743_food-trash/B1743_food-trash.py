import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M or not arr[ni][nj] or visited[ni][nj]: continue
            q.append((ni, nj))
            cnt += 1
            visited[ni][nj] = 1
    return cnt


N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(lambda x: int(x)-1, input().split())
    arr[r][c] = 1

visited = [[0] * M for _ in range(N)]
mmax = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] and not visited[i][j]:
            mmax = max(mmax, bfs(i, j))
print(mmax)