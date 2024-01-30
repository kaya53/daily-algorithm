from collections import deque


def ff(land, visited, si, sj, n, m):
    q = deque([(si, sj)])
    visited[si][sj] = 1
    rows = set()  # 이 부분을 카운트배열에서 set으로 바꾸니까 통과함

    size = 1
    while q:
        ci, cj = q.popleft()
        rows.add(cj)

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m or not land[ni][nj] or visited[ni][nj]: continue
            visited[ni][nj] = 1
            size += 1
            q.append((ni, nj))
    return rows, size


def solution(land):
    n = len(land)
    m = len(land[0])

    visited = [[0] * m for _ in range(n)]
    result = [0] * m
    for i in range(n):
        for j in range(m):
            if land[i][j] and not visited[i][j]:
                rows, size = ff(land, visited, i, j, n, m)
                for k in rows:
                    result[k] += size
    return max(result)
