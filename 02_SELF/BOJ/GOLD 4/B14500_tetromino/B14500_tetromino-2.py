import sys

sys.stdin = open('input.txt')

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def dfs(depth, ci, cj, tot, arr, visited, n, m, maxV):
    global answer
    if answer >= tot + (3-depth)*maxV: return

    if depth == 3:
        if answer < tot:
            answer = tot
            # print(tot)
            # print(visited)
        return
    for di, dj in delta:
        ni, nj = ci + di, cj + dj
        if ni < 0 or ni >= n or nj < 0 or nj >= m or (ni, nj) in visited: continue
        if depth == 1:
            dfs(depth+1, ci, cj, tot+arr[ni][nj], arr, visited+[(ni, nj)], n, m, maxV)
        dfs(depth + 1, ni, nj, tot+arr[ni][nj], arr, visited+[(ni, nj)], n, m, maxV)


def solution():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    maxV = 0
    for a in arr:
        maxV = max(maxV, max(a))

    for i in range(n):
        for j in range(m):
            visited = [(i, j)]
            dfs(0, i, j, arr[i][j], arr, visited, n, m, maxV)


# for _ in range(3):
answer = 0
solution()
print(answer)