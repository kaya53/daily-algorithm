import sys

sys.stdin = open('input.txt')


def dfs(idx, i, j, ssum):
    global res
    # 가지치기하니까 3배 정도 줄었음
    if res >= ssum + max_val*(4-idx): return
    if idx == 4:
        res = max(res, ssum)
        return
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj]: continue
        if idx == 2:
            visited[ni][nj] = 1
            dfs(idx + 1, i, j, ssum + arr[ni][nj])
            visited[ni][nj] = 0
        visited[ni][nj] = 1
        dfs(idx+1, ni, nj, ssum+arr[ni][nj])
        visited[ni][nj] = 0



# for _ in range(3):
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
# other_dir = [[(0, 1), (-1, 1), (0, 2)], [(0, 1), (1, 1), (0, 2)], [(1, 0), (2, 0), (1, 1)], [(1, 0), (2, 0), (1, -1)]]
res = 0
max_val = max(map(max, arr))
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        choice = [(i, j), 0, 0, 0]
        dfs(1, i, j, arr[i][j])
        # 한번 할 때마다 visited 초기화
        visited[i][j] = 0

print(res)
