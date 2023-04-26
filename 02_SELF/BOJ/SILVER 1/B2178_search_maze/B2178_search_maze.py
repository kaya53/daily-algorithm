# sys.stdin.readline은 개행문자까지 모두 입력받아 오기 때문에
# rstrip()을 같이 써주는 것이 좋다

import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs():
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((0, 0, 1))
    visited[0][0] = 1
    # dist = 0
    while q:
        ci, cj, dist = q.popleft()
        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M or not arr[ni][nj] or visited[ni][nj]: continue
            if (ni, nj) == (N - 1, M - 1): return dist+1
            q.append((ni, nj, dist+1))
            visited[ni][nj] = 1


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# for _ in range(4):
N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

print(bfs())


# 다른 bfs
# def bfs():
#     visited = [[0] * M for _ in range(N)]
#     q = deque()
#     q.append((si, sj))
#     visited[si][sj] = 1
#     dist = 1
#     while q:
#         dist += 1
#         for _ in range(len(q)):
#             ci, cj = q.popleft()
#             for di, dj in delta:
#                 ni, nj = ci + di, cj + dj
#                 if ni < 0 or ni >= N or nj < 0 or nj >= M or not arr[ni][nj] or visited[ni][nj]: continue
#                 if (ni, nj) == (N - 1, M - 1): return dist
#                 q.append((ni, nj))
#                 visited[ni][nj] = 1