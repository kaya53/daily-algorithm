import sys

sys.stdin = open('input.txt')

import heapq

n, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
INF = int(1e5)
# visited = [[[INF, INF] for _ in range(n)] for _ in range(n)]  # 최소 일사량, 거리
visited = [[INF]*n for _ in range(n)]  # 최소 일사량, 거리
# 출발점, 도착점 찾기
si = sj = ei = ej = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == -1:
            si, sj = i, j
            # visited[i][j] = -1
        elif arr[i][j] == -2:
            ei, ej = i, j

hq = []
res = 0
heapq.heappush(hq, (0, 0, si, sj))  # 최소 일사량, 출발점부터의 거리, 현재 좌표
while hq:
    solar, time, ci, cj = heapq.heappop(hq)
    if time > t:
        continue
    if ci == ei and cj == ej:
        res = solar + 2
        print(res)
        break
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = ci + di, cj + dj
        # 인덱스 밖, 건물, 출발점은 건너뛰기
        if ni < 0 or ni >= n or nj < 0 or nj >= n or not arr[ni][nj] or arr[ni][nj] == -1: continue
        # if visited[ni][nj][0] > solar + arr[ni][nj] or visited[ni][nj][1] > time + 1:  # 최소 일사량
        if visited[ni][nj] > time + 1:  # 최소 일사량

            # visited[ni][nj][0] = solar + arr[ni][nj]
            visited[ni][nj] = time + 1
            # visited[ni][nj][1] = time + 1
            heapq.heappush(hq, (solar + arr[ni][nj], time + 1, ni, nj))

else:
    print(-1)
