import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs():
    if info.get((0, 0), -1) == -1: return
    visited = [[0] * N for _ in range(N)]  # 들여다본 방 모두 표시

    visited[0][0] = 1
    arr[0][0] = 1  # 불 켜기
    q = deque()
    q.append((0, 0))

    cnt = 1
    while q:
        ci, cj = q.popleft()
        # 불 켜기
        if info.get((ci, cj), -1) != -1:
            for ii, jj in info[(ci, cj)]:
                # 이전에 들여다 본 방인데, 불이 꺼져 있는 방 => 새로 불을 켠 방 
                # 큐에 넣어서 관리하기
                if visited[ii][jj] == 1 and arr[ii][jj] == 0: 
                    q.append((ii, jj))
                if arr[ii][jj] == 0:
                    arr[ii][jj] = 1
                    cnt += 1

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]: continue
            visited[ni][nj] = 1
            if arr[ni][nj]: # 불이 켜져 있는 곳
                q.append((ni, nj))
    return cnt


# for _ in range(3):
N, M = map(int, input().split())
info = {}  # 스위치가 있는 방: 여기서 켤 수 있는 방 좌표

for _ in range(M):
    si, sj, ei, ej = map(lambda x: int(x) - 1, input().split())
    if info.get((si, sj), -1) == -1:
        info[(si, sj)] = []
    info[(si, sj)].append((ei, ej))

arr = [[0] * N for _ in range(N)]  # 불이 켜져있는 지 꺼져있는 지 관리
res = bfs()

print(res)