# 230524 python 554ms : 40분
# 유의할 점
# 1. 계란틀 이동하는 횟수 카운팅 시점
# => bfs 한번 돌 때마다가 아니라 모든 격자에 대해 가능한 이동을 모두 해봤으면 그 때 +1을 해야함
# 2. 합쳐질 계란틀이 구해지면 이동시키는 게 아니라 모든 격자 탐색이 끝나면 동시에 해줘야 함
import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs(si, sj):
    q = deque([(si, sj)])
    visited[si][sj] = 1
    whole = arr[si][sj]
    cnt = 1
    egg_ls = [[si, sj]]

    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]: continue
            if L <= abs(arr[ci][cj] - arr[ni][nj]) <= R:
                q.append((ni, nj))
                visited[ni][nj] = 1
                egg_ls.append([ni, nj])
                whole += arr[ni][nj]
                cnt += 1

    # 이동이 일어난 경우
    if cnt > 1:
        calced = int(whole / cnt)
        # print(whole, cnt)
        for k in range(len(egg_ls)):
            egg_ls[k].append(calced)
        # print(egg_ls)
        return egg_ls
    return []


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

res = 0
while True:
    combined = []
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                ls = bfs(i, j)
                combined += ls
    if not combined:
        print(res)
        break
    res += 1

    # 합치기
    for coi, coj, num in combined:
        arr[coi][coj] = num

