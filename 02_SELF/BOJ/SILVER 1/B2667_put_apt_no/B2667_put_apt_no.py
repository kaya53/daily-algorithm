import sys
sys.stdin = open('input.txt')
from collections import deque


def ff(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >=N or not arr[ni][nj] or visited[ni][nj]: continue
            q.append((ni, nj))
            visited[ni][nj] = 1
            cnt += 1
    return cnt


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

whole = 0
res = []
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] and not visited[i][j]:
            res.append(ff(i, j))
            whole += 1
res.sort()
print(whole, *res, sep='\n')