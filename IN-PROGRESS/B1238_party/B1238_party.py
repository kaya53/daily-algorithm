# 소요시간 1시간 pypy 3984ms, python 시간 초과
# (1 ~ N) 에서 x까지 가는 경우를 구할 때 매번 다익스트라를 돌렸는데
# 여기서 줄일 수 있는 방법이 있을 것 같다
import sys

sys.stdin = open('input.txt')

from collections import deque


def dijkstra(s):
    visited = [int(1e9)] * N
    q = deque([(s, 0)])
    visited[s] = 0

    while q:
        curr, dist = q.popleft()

        for ni in range(N):
            if not adj[curr][ni]: continue
            now = dist + adj[curr][ni]
            if visited[ni] > now:
                visited[ni] = now
                q.append((ni, now))
    if s != X-1: return visited[X-1]
    return visited


N, M, X = map(int, input().rstrip().split())
adj = [[0]*N for _ in range(N)]
for _ in range(M):
    k, e, t = map(int, input().rstrip().split())
    adj[k-1][e-1] = t

answer = [0] * N
for p in range(N):
    res = dijkstra(p)  # p에서 다른 점까지
    if p != X-1:
        answer[p] += res
    else:
        for r in range(N):
            answer[r] += res[r]
print(max(answer))
