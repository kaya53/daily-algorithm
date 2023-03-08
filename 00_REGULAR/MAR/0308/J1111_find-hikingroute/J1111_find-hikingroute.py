import sys

sys.stdin = open('input.txt')

from collections import deque

n = int(input())
ti, tj = map(int, input().split())
mountain = [list(map(int, input().split())) for _ in range(n)]
INF = int(1e9)
visited = [[INF] * n for _ in range(n)]

q = deque()
q.append((ti-1, tj-1))
visited[ti-1][tj-1] = 0
mmin = INF


while q:
    ci, cj = q.popleft()
    if ci == 0 or cj == 0 or ci == n-1 or cj == n-1:  # 여기에 0일 때만 넣어줘서 틀렸었음
        if mmin > visited[ci][cj] + mountain[ci][cj] ** 2:
            mmin = visited[ci][cj] + mountain[ci][cj] ** 2

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = ci + di, cj + dj
        if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
        now_height = mountain[ci][cj]
        next_height = mountain[ni][nj]
        tot_weight = 0  # 평지
        if now_height < next_height:  # 내리막길
            tot_weight = next_height - now_height
        elif now_height > next_height:  # 오르막길
            tot_weight = (now_height - next_height)**2

        std = visited[ni][nj]
        if std > visited[ci][cj] + tot_weight:
            visited[ni][nj] = visited[ci][cj] + tot_weight
            q.append((ni, nj))

print(mmin)

for elem in visited:
    print(elem)