import sys
from collections import deque
# sys.stdin = open('input.txt')


def bfs(si, sj):
    q = deque()
    q.append((si, sj, 0))
    visited = [[0]*n for _ in range(n)]
    visited[si][sj] = 1
    end = []
    min_dist = int(1e9)
    while q:
        for _ in range(len(q)):
            ci, cj, dist = q.popleft()
            if dist >= min_dist:
                arr[end[0]][end[1]] = 0
                return end
            if arr[ci][cj] == 1:
                min_dist = dist
                if end:
                    if end[0] > ci or (end[0] == ci and end[1] > cj):
                        end = [ci, cj]
                else:
                    end = [ci, cj]
                continue
            for di, dj in delta:
                ni, nj = ci+di, cj+dj
                if ni < 0 or ni >= n or nj < 0 or nj >= n or visited[ni][nj]: continue
                visited[ni][nj] = 1
                q.append((ni, nj, dist+1))


delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]  # 1: 베캠

base = [0] * m
base_q = [0] * m
conv = [0] * m
for k in range(m):
    coni, conj = map(lambda x: x-1, map(int, input().split()))
    conv[k] = [coni, conj]
    res = bfs(coni, conj)
    base[k] = res
arr = [[0] * n for _ in range(n)]

time = cnt = 0
while True:
    time += 1
    if time <= m:
        # 베이스 캠프로 들어오기
        arr[base[time - 1][0]][base[time - 1][1]] = -1
        base_q[time-1] = deque([base[time-1]])
    # 격자에 있는 사람들 이동하기
    # arr을 돌면서 -1이 아니면 상좌우하 순으로 한 칸씩 옮기기 -> 딕셔너리 쓰자(여러명이 한칸에 있을 수도 있기 떄문)
    # 한칸씩 옮기다가 편의점에 도착하면 cnt + 1
    for idx, now_q in enumerate(base_q):
        if idx == time - 1: continue
        while now_q:
            visited = [[0] * n for _ in range(n)]
            flag = False
            for _ in range(len(now_q)):
                ci, cj = now_q.popleft()
                for di, dj in delta:
                    ni, nj = ci + di, cj + dj
                    if ni < 0 or ni >= n or nj < 0 or nj >= n or arr[ni][nj] == -1: continue
                    if visited[ni][nj]: continue
                    if (ni, nj) == (conv[idx][0], conv[idx][1]):  # 편의점 도착
                        cnt += 1
                        arr[ni][nj] = -1
                        base_q[idx] = []  # q 비우기
                        flag = True
                        break
                    now_q.append((ni, nj))
                    visited[ni][nj] = 1
                    base[idx] = [ni, nj]  # 위치 갱신
                if flag: break
            break
    if cnt == m:
        print(time)
        break