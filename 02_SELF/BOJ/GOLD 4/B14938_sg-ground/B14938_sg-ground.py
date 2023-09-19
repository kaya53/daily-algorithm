# 소요시간: 의미 없음 => python 52ms
# 다익스트라, 플로이드-워셜을 써야하는 문제
# 최단 경로로 풀어야 하는 이유
# - 최단 경로로 해야 수색 경로 내에 있는 노드를 정상적으로 찾을 수 있다
# - 그렇기 때문에 다익스트라, 플로이드-워셜을 써야함
import sys
import heapq

sys.stdin = open('input.txt')


def dijkstra(s):
    q = []
    dist = [int(1e9)] * N
    heapq.heappush(q, (s, 0))  # 시작 노드, 거리
    dist[s] = 0

    while q:
        now, now_dist = heapq.heappop(q)

        if dist[now] < now_dist: continue

        for nnext, n_dist in graph[now]:
            cost = now_dist+n_dist
            if cost < dist[nnext]:
                dist[nnext] = cost
                heapq.heappush(q, (nnext, cost))
    return dist


# 노드 수, 수색 범위, 간선 수
N, M, R = map(int, input().rstrip().split())
items = list(map(int, input().rstrip().split()))

graph = [[] for _ in range(N)]
for _ in range(R):
    s, e, v = map(int, input().rstrip().split())
    s -= 1
    e -= 1
    graph[s].append((e, v))
    graph[e].append((s, v))

maxV = 0
for i in range(N):
    res = dijkstra(i)
    nowV = 0
    for z in range(N):
        if res[z] <= M: nowV += items[z]
    if maxV < nowV: maxV = nowV
print(maxV)


