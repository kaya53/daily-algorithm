import sys
import heapq
sys.stdin = open('input.txt')

INF = int(1e9)
N, M, S = map(int, input().split())
S -= 1
graph = [[0] * N for _ in range(N)]
for _ in range(M):
    s, e, v = map(int, input().split())
    graph[s-1][e-1] = v

q = [(S, 0)]
dist = [INF] * N
dist[S] = 0
while q:
    now, d = heapq.heappop(q)
    # print(now)
    if dist[now] < d: continue
    for nnext, val in enumerate(graph[now]):
        # print(nnext)
        if not graph[now][nnext]: continue  # 다음 도시로 갈 길이 없으면 continue
        cost = d + val
        if dist[nnext] > cost:
            dist[nnext] = cost
            heapq.heappush(q, (nnext, cost))

res = 0
time = 0
for i in range(N):
    if 0 < dist[i] < INF:
        res += 1
        if time < dist[i]:
            time = dist[i]
print(res, time)


