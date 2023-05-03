import sys

sys.stdin = open('input.txt')

from collections import deque

def bfs(si, sj, w, s):
    global wolf, sheep
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            k = 0
            ni, nj = ci, cj
            while (0 <= ni < N) and (0 <= nj < M):
                k += 1
                ni, nj = ci + di*k, cj + dj*k
                if ni < 0 or ni >= N or nj < 0 or nj >= M or visited[ni][nj]: continue
                if arr[ni][nj] == '#': break  # 울타리 너머는 갈 수 없음
                if arr[ni][nj] == 'v': w += 1
                elif arr[ni][nj] == 'o': s += 1
                visited[ni][nj] = 1
                q.append((ni, nj))
    # print(w, s)
    if w < s: wolf -= w
    else: sheep -= s
    # for v in visited:
    #     print(v)


# for _ in range(3):
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
wolf = sheep = 0
for a in arr:
    for r in a:
        if r == 'v': wolf += 1
        elif r == 'o': sheep += 1

visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'v' and not visited[i][j]:
            bfs(i, j, 1, 0)
        elif arr[i][j] == 'v' and not visited[i][j]:
            bfs(i, j, 0, 1)
print(sheep, wolf)