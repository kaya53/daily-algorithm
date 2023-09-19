import sys
import heapq

sys.stdin = open('input.txt')


def dijkstra(start):
    q = [(start, 0)]
    dist = [INF] * N

    while q:
        now, now_dist = heapq.heappop(q)

        for nnext in graph[now]:
            if dist[nnext] > now_dist + 1:
                dist[nnext] = now_dist + 1
                heapq.heappush(q, (nnext, now_dist+1))
    # print(dist)
    return dist


INF = int(1e9)
# for _ in range(2):
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    s, e = map(lambda x: int(x)-1, input().split())
    graph[s].append(e)
    graph[e].append(s)
end, mid = map(lambda x: int(x)-1, input().split())

mid_ls = dijkstra(1)
end_ls = dijkstra(mid)
res = mid_ls[mid] + end_ls[end]
if res >= INF: print(-1)
else: print(res)