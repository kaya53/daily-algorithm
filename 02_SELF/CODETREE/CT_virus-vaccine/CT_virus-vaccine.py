# 230524 python 282ms => 1시간 소요
# 코드 작성 30분, 디버깅 30분 소요
# 유의할 점
# 1. 선택되지 않은 병원이 도착점일 경우 바이러스가 퍼진 시간으로 치면 안됨
# 2. 바이러스가 없는 경우는 bfs를 돌릴 필요가 없으므로 시작도 안해도 됨; 하기도 전에 끝
# 3. 바이러스가 모두 박멸된 이후에만 최소 시간을 갱신

import sys

sys.stdin = open('input.txt')

from collections import deque


def comb(idx, ci):
    if idx == M:
        visited = [[0] * N for _ in range(N)]
        for chi, chj in choice:
            arr[chi][chj] = 2
            visited[chi][chj] = -1
        bfs(choice, visited)

        for chi, chj in choice:
            arr[chi][chj] = 0
        return

    for ni in range(ci, total_hos):
        choice[idx] = hospital[ni]
        comb(idx+1, ni+1)
        choice[idx] = 0


def bfs(chq, visited):
    global res_min

    # 병원이 시작점
    q = deque(chq)
    now_zero = zero_cnt

    t = 0
    while q:
        t += 1
        for _ in range(len(q)):
            ci, cj = q.popleft()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj] != 0: continue
                if not arr[ni][nj]:
                    q.append((ni, nj))
                    if (ni, nj) in hospital: visited[ni][nj] = -1
                    else:
                        now_zero -= 1
                        visited[ni][nj] = t

    if not now_zero:
        now_time = 0
        for v in visited:
            now_time = max(now_time, max(v))
        res_min = min(res_min, now_time)


# for _ in range(5):
N, M = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]
hospital = []
total_hos = 0
zero_cnt = 0
for r in range(N):
    inp = list(map(int, input().split()))
    arr[r] = inp
    for c in range(N):
        if inp[c] == 2:
            hospital.append((r, c))
            arr[r][c] = 0
            total_hos += 1
        elif inp[c] == 0:
            zero_cnt += 1

# 병원으로 선택된 것들
# print(zero_cnt, tot_hos_zero)
if zero_cnt:
    choice = [0] * M
    res_min = int(1e9)
    comb(0, 0)
    if res_min == int(1e9):
        print(-1)
    else:
        print(res_min)
else:
    print(0)