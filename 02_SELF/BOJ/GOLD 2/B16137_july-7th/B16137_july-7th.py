# 230524 python 68ms => 2시간 소요; 7번만에 맞음
# 1. 교차 체크하는 방법
# 내가 사용한 방법: 양 옆에 0이 있다면 다른 양 옆에는 1이 있을 때만 놓을 수 있는 절벽으로 본다.
# => 문제점
# 1) 인덱스 에러가 남 
# 2) 절벽이 모두 땅으로 둘러싸여 있는 경우는 잡아내지 못함
# 선생님이 알려주신 방법: 탐색하고 있는 절벽을 기준으로 'ㄴ'자 모양으로 절벽이 있으면 볼 수 없는 절벽

# 2. 오작교를 두 번 연속으로 방문할 수 없음!

import sys

sys.stdin = open('input.txt')

from collections import deque


def find_possible_cliff():
    cliff = []

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                for di, dj, ddi, ddj in check_delta:
                    ni, nj, nni, nnj = r+di, c+dj, r+ddi, c+ddj
                    if ni < 0 or ni >= N or nj < 0 or nj >= N or nni < 0 or nni >= N or nnj < 0 or nnj >= N: continue
                    if arr[ni][nj] == 0 and arr[nni][nnj] == 0: continue
                    cliff.append((r, c))
    return cliff


def bfs():
    visited = [[-1] * N for _ in range(N)]
    q = deque([(0, 0, 1, False)])
    visited[0][0] = -2
    
    while q:
        ci, cj, time, is_crossed = q.popleft()
        if (ci, cj) == (N-1, N-1): return visited[N-1][N-1]

        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            # 인덱스 밖, 절벽, 이미 방문한 곳 제외
            if ni < 0 or ni >= N or nj < 0 or nj >= N or not arr[ni][nj] or visited[ni][nj] != -1: continue
            if arr[ni][nj] > 1 and is_crossed is False:  # 오작교 + 직전에 오작교를 지나오지 않음
                if time % arr[ni][nj] == 0:  # 주기가 되서 지나갈 수 있음
                    q.append((ni, nj, time+1, True))
                    visited[ni][nj] = time
                else: q.append((ci, cj, time+1, False))  # 기다리기
            elif arr[ni][nj] == 1:  # 땅이라 지나갈 수 있음
                q.append((ni, nj, time + 1, False))
                visited[ni][nj] = time


check_delta = [(-1, 0, 0, -1), (-1, 0, 0, 1), (1, 0, 0, -1), (1, 0, 0, 1)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# for _ in range(3):
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 오작교를 놓을 수 있는 절벽 찾기 => 교차 판별
poss_cliff = find_possible_cliff()
# print(poss_cliff)

# 오작교 하나씩 놓아보기
mmin = int(1e9)
for pi, pj in poss_cliff:
    arr[pi][pj] = M
    res = bfs()
    if res: mmin = min(mmin, res)
    arr[pi][pj] = 0
print(mmin)