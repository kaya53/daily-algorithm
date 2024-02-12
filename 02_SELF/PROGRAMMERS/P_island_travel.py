from collections import deque


def bfs(n, m, maps, visited, si, sj):
    q = deque([(si, sj)])
    tot = maps[si][sj]
    while q:
        ci, cj = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
            if visited[ni][nj] or maps[ni][nj] == 'X': continue
            visited[ni][nj] = 1
            tot += maps[ni][nj]
            q.append((ni, nj))
    return tot


def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])

    for r in range(n):
        tmp = []
        for c in range(m):
            if maps[r][c] == 'X':
                tmp.append('X')
            else:
                tmp.append(int(maps[r][c]))
        maps[r] = tmp[:]

    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                visited[i][j] = 1
                r = bfs(n, m, maps, visited, i, j)
                answer.append(r)
    if answer:
        return sorted(answer)
    return [-1]
