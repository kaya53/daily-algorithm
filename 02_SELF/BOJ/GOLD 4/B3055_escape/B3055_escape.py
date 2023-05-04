# 230503 python 72ms
# 다른 방법:
# visited에 물이 퍼진 시간을 저장하고, 고슴도치가 이동한 시간을 비교해서 고슴도치가 더 먼저 도착했으면 이동할 수 있도록 처리해도 된다
# => 근데 이 방법은 물을 무조건 다 퍼뜨려야 하므로 시간이 더 소요될 수 있다.
import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs(si, sj, water_q):
    cock_q = deque()
    cock_q.append((si, sj))
    visited[si][sj] = 1
    time = -1
    while True:
        time += 1
        # 물 먼저 퍼뜨리고
        while water_q:
            for _ in range(len(water_q)):  # 동일 너비에 대한 처리
                wi, wj = water_q.popleft()
                for dwi, dwj in delta:
                    nwi, nwj = wi + dwi, wj + dwj
                    if nwi < 0 or nwi >= R or nwj < 0 or nwj >= C or arr[nwi][nwj] != '.': continue
                    water_q.append((nwi, nwj))
                    arr[nwi][nwj] = '*'
            break
            
        # 고슴도치 이동 시키기
        while cock_q:
            for _ in range(len(cock_q)):
                ci, cj = cock_q.popleft()
                if (ci, cj) == (ei, ej): return time

                for di, dj in delta:
                    ni, nj = ci + di, cj + dj
                    if ni < 0 or ni >= R or nj < 0 or nj >= C or visited[ni][nj]: continue
                    if arr[ni][nj] == '*' or arr[ni][nj] == 'X': continue
                    cock_q.append((ni, nj))
                    visited[ni][nj] = 1
            break
            
        # 고슴도치가 가능한 이동을 모두 끝냈는 데도 return time을 만나지 않았을 때
        if not cock_q: return 'KAKTUS'


delta = [(0, -1), (0, 1), (-1, 0), (1, 0)]
# for _ in range(4):
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

si, sj = 0, 0
ei, ej = 0, 0
water_q = deque()
# 고슴도치 시작점, 물 찾기
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'S': si, sj = i, j
        elif arr[i][j] == 'D': ei, ej = i, j
        elif arr[i][j] == '*': water_q.append((i, j))

visited = [[0] * C for _ in range(R)]
print(bfs(si, sj, water_q))
