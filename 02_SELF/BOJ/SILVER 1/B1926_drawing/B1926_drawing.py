import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    cnt = 1
    visited[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M or not arr[ni][nj] or visited[ni][nj]: continue
            q.append((ni, nj))
            cnt += 1
            visited[ni][nj] = 1
    return cnt


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

w_cnt = 0
mmax = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] and not visited[i][j]:
            mmax = max(mmax, bfs(i, j))
            w_cnt += 1
print(w_cnt, mmax, sep='\n')

# ls = [0, 1] * 250
# ls2 = [1, 0] * 250
# lls = []
# for _ in range(250):
#     lls.append(ls)
#     lls.append(ls2)
# for l in lls:
#     print(*l)