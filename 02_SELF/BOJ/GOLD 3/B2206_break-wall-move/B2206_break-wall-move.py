import sys
# sys.stdin = open('input.txt')
from collections import deque

input = sys.stdin.readline

# for _ in range(2):
n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [[[-1, -1] for _ in range(m)] for _ in range(n)]  # 벽을 안부쉈을 때, 부쉈을 때
visited[0][0] = [1, 1]
q = deque()
q.append((0, 0, 0, 1))  # flag = 0, 아직 부순 벽이 없는 것

while q:
    ci, cj, flag, cnt = q.popleft()
    if ci == n-1 and cj == m-1:
        print(visited[ci][cj][flag])
        break

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = ci + di, cj + dj
        if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
        if arr[ni][nj] == 1:
            if flag == 0:  # 벽 부수기
                if visited[ni][nj][1] == -1:
                    visited[ni][nj][1] = cnt + 1
                    q.append((ni, nj, 1, cnt + 1))
            continue

        if visited[ni][nj][flag] == -1:
            visited[ni][nj][flag] = cnt + 1
            q.append((ni, nj, flag, cnt + 1))

else:
    print(-1)

for e in visited:
    print(e)