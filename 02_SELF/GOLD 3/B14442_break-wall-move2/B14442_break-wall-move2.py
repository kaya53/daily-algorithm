import sys
from collections import deque
# sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]

visited[0][0] = [1]*(k+1)
q = deque()
q.append((0, 0, 0, 1))  # 현재 좌표, 부순 횟수, 최단 경로

while q:
    ci, cj, broken, dist = q.popleft()

    if ci == n-1 and cj == m-1:
        print(visited[ci][cj][broken])
        break

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = ci + di, cj + dj
        if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
        if not arr[ni][nj]: # 길
            if not visited[ni][nj][broken]: # 어떤 식으로든 방문한 적 없음
                visited[ni][nj][broken] = dist+1
                q.append((ni, nj, broken, dist+1))
            # 방문한 적은 있는 데 지금 경로가 더 최단이라면
            elif visited[ni][nj][broken] and visited[ni][nj][broken] > dist + 1:
                visited[ni][nj][broken] = dist+1
                q.append((ni, nj, broken, dist+1))
        else:
            if broken + 1> k: continue
            if not visited[ni][nj][broken]:  # 어떤 식으로든 방문한 적 없음
                visited[ni][nj][broken] = dist + 1
                q.append((ni, nj, broken+1, dist + 1))
            # 방문한 적은 있는 데 지금 단계에서 방문한게 아니고..? 지금 경로가 더 최단이라면
            elif visited[ni][nj][broken] and visited[ni][nj][broken] > dist + 1:
                visited[ni][nj][broken] = dist + 1
                q.append((ni, nj, broken+1, dist + 1))
else:
    print(-1)