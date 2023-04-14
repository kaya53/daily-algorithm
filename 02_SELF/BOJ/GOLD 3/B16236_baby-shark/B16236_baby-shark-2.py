# 먹을 수 있는 물고기의 마리수를 "공간 전체"에서 세야 한다.
# 한번 이동할 때 4방에 먹을 수 있는 물고기가 몇 마리인지를 세는 것이 아니다


import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def baby_shark():
    global shi, shj, res_cnt

    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((shi, shj, 0))
    visited[shi][shj] = 1
    fish = []

    while q:
        for _ in range(len(q)):
            ci, cj, t = q.popleft()
            for di, dj in delta:
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj] == 1: continue
                if arr[ni][nj] > size: continue
                q.append((ni, nj, t+1))
                visited[ni][nj] = 1

                if 0 < arr[ni][nj] < size:
                    # 여기서 priority queue를 써도 되지만 넣을 때마다 O(nlogn)의 연산이 일어나고
                    # 이 문제에서는 정렬을 한 번만 해주면 되서 배열로 해결함
                    fish.append((t+1, ni, nj))

    if fish:
        fish.sort()  # 시간(거리) 짧은 순, 행 짧은 순, 열 짧은 순 
        shi, shj = fish[0][1:]  # 상어 위치 갱신
        arr[shi][shj] = 0
        res_cnt += 1
        return fish[0][0]
    return False


delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]
# for _ in range(6):
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

shi, shj, size = 0, 0, 2
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shi, shj = i, j
            arr[i][j] = 0

res_time = res_cnt = 0
while True:
    r = baby_shark()  # 모든 격자를 돌면서 물고기를 1마리 먹으려 할 때 최단으로 걸리는 시간
    if r is not False:  
        res_time += r
        if res_cnt == size:
            size += 1
            res_cnt = 0
    else: # 공간 전체에 먹을 물고기가 없는 경우
        print(res_time)
        break
