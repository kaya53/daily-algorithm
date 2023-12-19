import sys

sys.stdin = open('input.txt')

from collections import deque


def solution():
    dist = [[[INF] * N for _ in range(N)] for _ in range(N)]
    v = [0] * N
    v[K] = 1
    q = deque([(K, 0, v)])
    for j in range(N):
        dist[0][K][j] = adj[K][j]

    while q:
        now, cost, visited = q.popleft()

        k = sum(visited) - 1
        for z in range(N):
            if now == z: continue
            nc = cost + adj[now][z]
            if not visited[z]:
                visited[z] = 1
                if dist[k+1][now][z] > nc:
                    dist[k+1][now][z] = nc
                    q.append((z, nc, visited[:]))
                visited[z] = 0
            else:
                if dist[k][now][z] > nc:
                    dist[k][now][z] = nc
                    q.append((z, nc, visited[:]))
    for d1 in dist:
        for d in d1:
            print(d)
        print()
    return dist[N-1]


for _ in range(2):
    N, K = map(int, input().split())
    adj = [list(map(int, input().split())) for _ in range(N)]
    INF = int(1e9)
    res = solution()

    answer = INF
    for r in res:
        v = min(r)
        if answer > v:
            answer = v
    print(answer)

