import sys

sys.stdin = open('input.txt')

from collections import deque


def solution(n, si, sj, stores, ei, ej):
    q = deque([(si, sj)])  # 위치
    visited = [0] * n  # 편의점 방문
    while q:
        ci, cj = q.popleft()
        # 20병으로 페스티벌 갈 수 있음
        if abs(ei-ci)+abs(ej-cj) <= 1000:
            return 'happy'
        for k in range(n):
            if visited[k]: continue
            ni, nj = stores[k]
            # 현재 시점에서 편의점까지 갈 수 있는 경우만
            if abs(ni-ci)+abs(nj-cj) <= 1000:
                q.append((ni, nj))
                visited[k] = 1
    return 'sad'


T = int(input())
for _ in range(T):
    N = int(input())
    SI, SJ, = map(int,input().split())
    S = [tuple(map(int, input().split())) for _ in range(N)]
    EI, EJ = map(int, input().split())
    r = solution(N, SI, SJ, S, EI, EJ)
    print(r)
