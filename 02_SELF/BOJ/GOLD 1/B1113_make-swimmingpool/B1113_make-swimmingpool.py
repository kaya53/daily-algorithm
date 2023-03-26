import sys
from collections import deque

# sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(si, sj, k, visited):
    global res

    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    min_wall = 10  # 경계 중 가장 낮은 벽
    for ti, tj in delta:
        tti, ttj = si+ti, sj+tj
        if (tti == 0 or tti == n - 1 or ttj == 0 or ttj == m - 1) and arr[tti][ttj] <= k:
            min_wall = k
            continue
        if arr[tti][ttj] < k:
            min_wall = k
            continue
        if arr[tti][ttj] == k: continue
        min_wall = min(min_wall, arr[tti][ttj])
    same_ls = [(si, sj)]

    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            if ni < 1 or ni >= n-1 or nj < 1 or nj >= m-1 or visited[ni][nj]: continue
            if (ni == 0 or ni == n-1 or nj == 0 or nj == m-1) and arr[ni][nj] <= k:
                min_wall = k
                continue
            if arr[ni][nj] != k: continue
            same_ls.append((ni, nj))
            q.append((ni, nj))
            visited[ni][nj] = 1
            # 주변에서 가장 작은 값 찾기
            for ddi, ddj in delta:
                nni, nnj = ni+ddi, nj+ddj
                if nni < 0 or nni >= n or nnj < 0 or nnj >= m: continue
                if (nni == 0 or nni == n-1 or nnj == 0 or nnj == m-1) and arr[nni][nnj] <= k:
                    min_wall = k
                    continue
                if arr[nni][nnj] == k: continue
                if arr[nni][nnj] < k:
                    min_wall = k
                    continue
                if min_wall > arr[nni][nnj]:
                    min_wall = arr[nni][nnj]
    if min_wall == 10: min_wall = k
    if min_wall != k:
        # print(same_ls, k, min_wall)
        for ii, jj in same_ls:
            res += min_wall - arr[ii][jj]
            arr[ii][jj] = min_wall


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# for _ in range(5):
n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

res = 0
for k in range(1, 10):
    for i in range(1, n-1):
        for j in range(1, m-1):
            if arr[i][j] == k:
                bfs(i, j, k, [[0] * m for _ in range(n)])

print(res)