import sys

sys.stdin = open('input.txt')


def dfs(ci, cj):
    if (ci, cj) == (N-1, M-1): return 1

    res = 0
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = ci + di, cj + dj
        if ni < 0 or ni >= N or nj < 0 or nj >= M: continue
        if arr[ni][nj] >= arr[ci][cj]: continue
        if memo[ni][nj] == -1:  # 아직 탐색이 안된 부분
            res += dfs(ni, nj)
        elif memo[ni][nj] > -1:
            res += memo[ni][nj]

    memo[ci][cj] = res
    return res


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

memo = [[-1] * M for _ in range(N)]
print(dfs(0, 0))
