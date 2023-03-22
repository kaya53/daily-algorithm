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
        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
            if not visited[ni][nj] and arr[ni][nj]:
                visited[ni][nj] = 1
                cnt += 1
                q.append((ni, nj))
    return cnt


n, m = map(int, input().split())  # i, j
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
res = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j]:
            if bfs(i, j):
                res += 1
print(res)