import sys
from collections import deque
sys.stdin = open('input.txt')


def baby_shark():
    global size

    q = deque()
    q.append((shi, shj))
    time = -1
    flag = False
    while q:
        time += 1
        ate = 0
        for _ in range(len(q)):
            ci, cj = q.popleft()
            for di, dj in delta:
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
                if arr[ni][nj] > size:
                    continue
                if arr[ni][nj] and arr[ni][nj] < size:
                    ate += 1
                    arr[ni][nj] = 0
                    q = deque([(ni, nj)]) # 한마리 먹었으면 끝
                    break
                q.append((ni, nj))  # 같은 경우 이동함
        if ate == size:
            size += 1
        for i in range(N):
            for j in range(N):
                if arr[i][j] and arr[i][j] < size:  # 먹을 수 있는 물고기 존재
                    flag = True
        if not flag:
            return time


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# for _ in range(6):
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

shi, shj, size = 0, 0, 2
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shi, shj = i, j
            arr[i][j] = 0

print(baby_shark())