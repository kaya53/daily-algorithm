# 소요시간 30분 pypy 1112ms python 3016ms
# 장애물이 움직이는 bfs

# => 가지치기 추가해서 python 1160ms까지 줄임
# 1. 8턴 이상 진행이 되면 무조건 가능 => 8턴 이상 가면 벽이 사라지기 때문
# 2. 벽이 없는 턴이 생기면 무조건 가능하게 리턴
import sys

sys.stdin = open('input.txt')

from collections import deque


def solution(arr):
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (-1, -1), (1, -1), (1, 1), (0, 0)]
    q = deque([(7, 0)])
    wall = set()
    for i in range(8):
        for j in range(8):
            if arr[i][j] == '#': wall.add((i, j))

    while q:
        if not wall: return 1
        for _ in range(len(q)):
            ci, cj = q.popleft()
            if (ci, cj) == (0, 7): return 1  # time > 8 이 넘으면 벽이 다 사라져서 가능함
            if (ci, cj) in wall: continue
            for di, dj in delta:
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= 8 or nj < 0 or nj >= 8 or (ni, nj) in wall: continue
                q.append((ni, nj))
        next_w = set()
        for ii, jj in wall:
            if ii < 7: next_w.add((ii+1, jj))
        wall = next_w
    return 0


for _ in range(5):
    print(solution([list(input()) for _ in range(8)]))