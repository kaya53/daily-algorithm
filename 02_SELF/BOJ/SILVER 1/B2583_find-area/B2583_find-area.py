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
            if ni < 0 or ni >= N or nj < 0 or nj >= M or arr[ni][nj] or visited[ni][nj]: continue
            q.append((ni, nj))
            visited[ni][nj] = 1
            cnt += 1
    return cnt


# 행, 열, 직사각형 좌표
N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]

for _ in range(K):
    sj, si, ej, ei = map(int, input().split())

    for ii in range(si, ei):
        for jj in range(sj, ej):
            arr[ii][jj] = 1

visited = [[0] * M for _ in range(N)]
res = 0
size = []
for i in range(N):
    for j in range(M):
        if not arr[i][j] and not visited[i][j]:
            size.append(ff(i, j))
            res += 1
size.sort()
print(res)
print(*size)