from collections import deque


def bfs(n, m, maps, si, sj, end):
    q = deque([(si, sj, 0)])  # 위치, 소요시간
    visited = [[0] * m for _ in range(n)]
    visited[si][sj] = 1

    while q:
        ci, cj, time = q.popleft()
        if maps[ci][cj] == end: return time

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m or maps[ni][nj] == 'X': continue
            if visited[ni][nj]: continue
            q.append((ni, nj, time + 1))
            visited[ni][nj] = 1
    return -1


def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])

    si, sj = -1, -1
    li, lj = -1, -1
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                si, sj = i, j
            elif maps[i][j] == 'L':
                li, lj = i, j
    to_lever = bfs(n, m, maps, si, sj, 'L')
    to_goal = bfs(n, m, maps, li, lj, 'E')
    if to_lever == -1 or to_goal == -1: return -1
    return to_lever + to_goal
