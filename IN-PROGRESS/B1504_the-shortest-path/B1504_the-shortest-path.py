# 소요시간 의미 없음 python 472ms, pypy 348ms
# 코드는 어렵지 않으나 아이디어? 수학적 고민?이 필요한 문제였음
# v1, v2를 반드시 거쳐서 1 ~ n까지 가야하는 거니까
# 1 ~ v1/v2 ~ v2/v1 ~ n 각 구간별 최단 거리를 구하고 각각 더해주면 된다!
import sys

sys.stdin = open('input.txt')

from heapq import heappop, heappush


def dijkstra(n, start, graph):
    hq = []
    heappush(hq, (0, start))
    visited = [200000001] * (n+1)
    visited[start] = 0
    while hq:
        tot, now = heappop(hq)

        # 이미 기록된 거리가 더 짧다면 이번 턴은 볼 필요가 없음
        if visited[now] < tot: continue

        for nnext, dist in graph[now]:
            if visited[nnext] > tot+dist:
                visited[nnext] = tot+dist
                heappush(hq, (tot+dist, nnext))

    return visited


def solution(n, m, paths, v1, v2):
    graph = [[] for _ in range(n+1)]
    for s, e, v in paths:
        graph[s].append((e, v))
        graph[e].append((s, v))
    
    # 1 ~ n까지 최단 거리 모음 => 여기서 1 ~ v1/v2까지 최단
    n_dist = dijkstra(n, 1, graph)
    # v1 ~ n까지 최단 거리 모음 => 여기서 v1 ~ v2/n까지 최단
    v1_dist = dijkstra(n, v1, graph)
    # v2 ~ n까지 최단 거리 모음 => 여기서 v2 ~ v1/n까지 최단
    v2_dist = dijkstra(n, v2, graph)

    # 각각 시작점이 다른 최단거리 리스트에서 필요한 정보만 뽑아내서 더하면 됨!
    ans1 = n_dist[v1] + v1_dist[v2] + v2_dist[n]
    ans2 = n_dist[v2] + v2_dist[v1] + v1_dist[n]

    if ans1 >= 200000001 or ans2 >= 200000001:
        return -1
    return min(ans1, ans2)




N, E = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(E)]
u, v = map(int, input().split())
print(solution(N, E, ls, u, v))