import sys

sys.stdin = open('input.txt')

from collections import deque
import heapq

def bfs(si, sj):
    q = deque()
    q.append((si, sj, 0))
    visited[0][0] = 1
    hq = []

    while q:
        ci, cj, time = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]: continue
            if size == arr[ni][nj]:  # 같은 건 지나만 간다
                q.append((ni, nj, time+1))
                visited[ni][nj] = 1
            elif size > arr[ni][nj]:  # 더 작은 건 지나도 가고
                q.append((ni, nj, time+1))
                visited[ni][nj] = 1
                if arr[ni][nj]:  # 0이 아니면 먹는다
                    heapq.heappush(hq, (time + 1, ni, nj))

    if hq:
        # print(hq)
        return heapq.heappop(hq)
    return 0


for _ in range(6):
    N = int(input())
    arr = [[] for _ in range(N)]

    si, sj = 0, 0
    size = 2
    for nn in range(N):
        inp = list(map(int, input().split()))
        arr[nn] = inp
        for mm in range(N):
            if inp[mm] == 9:
                si, sj = nn, mm
                arr[si][sj] = 0

    cnt = 0
    res = 0
    while True:
        visited = [[0] * N for _ in range(N)]
        move = bfs(si, sj)
        # print(size, move)
        if not move: break
        # 물고기 잡음
        t, si, sj = move
        res += t  # 시간 갱신
        cnt += 1
        arr[si][sj] = 0  # 물고기 냠냠
        # 크기 증가
        if size == cnt:
            size += 1
            cnt = 0
    print(res)