import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs(maze):
    while queue:
        ci, cj, time = queue.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if (ni < 0 or ni >= I) or (nj < 0 or nj >= J):
                continue
            if maze[ni][nj] == 0:
                if ni == ei and nj == ej:
                    return time + 1
                maze[ni][nj] = time + 1
                queue.append((ni, nj, time + 1))
    return maze[ei][ej]  # 도착을 못하는 경우

J, I = map(int, input().split())
sj, si, ej, ei = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(I)]

# 헷갈리기 싫어!
si -= 1
sj -= 1
ei -= 1
ej -= 1

queue = deque()
queue.append((si, sj, 0))
maze[si][sj] = 1  # 첫 칸도 방문 표시 필수
print(bfs(maze))

