# 소요시간 1시간 pypy 3984ms, python 시간 초과
# - (1 ~ N) 에서 x까지 가는 경우를 구할 때 매번 다익스트라를 돌렸는데
# 여기서 줄일 수 있는 방법이 있을 것 같다
# => 인접리스트 방향을 뒤집어서 또 만들면 된다! 이렇게 하면 python 260ms로 통과
# - priorityqueue 대신 좀 더 빠른 heapq 사용!
import sys

sys.stdin = open('input.txt')

# from collections import deque
import heapq


def dijkstra(adj):
    visited = [int(1e9)] * N
    hq = [(X-1, 0)]
    visited[X-1] = 0

    while hq:
        curr, dist = heapq.heappop(hq)

        if visited[curr] < dist: continue

        for ni in range(N):
            if not adj[curr][ni]: continue
            now = dist + adj[curr][ni]
            if visited[ni] > now:
                visited[ni] = now
                heapq.heappush(hq, (ni, now))
    return visited


N, M, X = map(int, input().rstrip().split())
adj_to = [[0]*N for _ in range(N)]
adj_from = [[0]*N for _ in range(N)]

for _ in range(M):
    k, e, t = map(int, input().rstrip().split())
    adj_to[e-1][k-1] = t  # 1~n에서 x까지 가는 거 뒤집기
    adj_from[k-1][e-1] = t

distance_to = dijkstra(adj_to)
distance_from = dijkstra(adj_from)
answer = 0
for i in range(N):
    if answer < distance_to[i]+distance_from[i]:
        answer = distance_to[i]+distance_from[i]

print(answer)