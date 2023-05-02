import sys

sys.stdin = open('input.txt')

from collections import deque

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= H or nj < 0 or nj >= W or not arr[ni][nj] or visited[ni][nj]: continue
            q.append((ni, nj))
            visited[ni][nj] = 1
    return 1


delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
while True:
    W, H = map(int, input().split())
    if (W, H) == (0, 0): break
    arr = []
    for _ in range(H):
        inp = list(map(int, input().split()))
        arr.append(inp)

    visited = [[0]* W for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if visited[i][j] or not arr[i][j]: continue
            cnt += bfs(i, j)
    print(cnt)
