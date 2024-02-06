# 도착지가 한 군데니까 도착지를 시작점으로 보면 bfs를 한번만 돌려도 됨
from heapq import heappush, heappop


def dijkstra(adj, end, n):
    hq = []
    heappush(hq, (0, end))
    distance = [int(1e9)] * (n + 1)
    distance[end] = 0

    while hq:
        dist, now = heappop(hq)
        # print(dist, now)

        if distance[now] < dist: continue

        for nnext in adj[now]:
            if distance[nnext] > dist + 1:
                distance[nnext] = dist + 1
                heappush(hq, (dist + 1, nnext))

    return distance


def solution(n, roads, sources, destination):
    answer = []
    adj = [[] for _ in range(n + 1)]
    for r, c in roads:  # 최대 50만 번
        adj[r].append(c)
        adj[c].append(r)
    result = dijkstra(adj, destination, n)
    for s in sources:
        if result[s] == int(1e9):
            answer.append(-1)
        else:
            answer.append(result[s])
    return answer