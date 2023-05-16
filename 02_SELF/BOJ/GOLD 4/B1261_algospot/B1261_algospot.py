import sys

sys.stdin = open('input.txt')

from collections import deque

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = 0
    
    while q:
        ci, cj, broken = q.popleft()
        # 여기에 가장 먼저 도달하는 것이 문제가 아니라 벽을 적게 깨는게 문제임
        # 더 적게 깨고 온 경우에만 visited 갱신
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M: continue
            tmp = broken
            if arr[ni][nj] == 1:
                tmp += 1

            if visited[ni][nj] > tmp:
                visited[ni][nj] = tmp
                q.append((ni, nj, tmp))


# for _ in range(3):
M, N = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

visited = [[N*M-2] * M for _ in range(N)]
bfs()

print(visited[-1][-1])
