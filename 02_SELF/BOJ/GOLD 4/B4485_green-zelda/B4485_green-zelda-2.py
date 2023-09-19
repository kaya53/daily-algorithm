# 소요시간: 20분: python3 88ms, pypy 204ms
# 전형적 다익스트라 문제 => 가중치가 있는 최단 경로
import sys

sys.stdin = open('input.txt')

import heapq

INF = int(1e9)
def dijkstra():
    q = [(arr[0][0], 0, 0)]
    visited = [[INF] * N for _ in range(N)]
    visited[0][0] = arr[0][0]

    while q:
        rupee, ci, cj = heapq.heappop(q)
        if (ci, cj) == (N-1, N-1): return visited[N-1][N-1]
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
            stolen = arr[ni][nj] + rupee
            if visited[ni][nj] > stolen:
                visited[ni][nj] = stolen
                heapq.heappush(q, (stolen, ni, nj))


tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0: break
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'Problem {tc}: {dijkstra()}')