import sys

sys.stdin = open('input.txt')

import heapq

v, e = map(int, input().split())
start = int(input())
INF = int(1e9)
distance = [INF] * (v+1)  # 시작 노드부터 이번 노드까지 최단 거리를 담을 배열

graph = [[] for _ in range(v+1)]  # 연결된 점과 가중치를 담을 방향 그래프
for _ in range(e):
    ui, vi, w = map(int, input().split())  # 연결 노드1, 연결 노드2, 가중치
    graph[ui].append((vi, w))
    # graph[v].append((u, w))


hq = []
distance[start] = 0  # 시작 노드에서 시작노드로 가는 거리는 0이니까
heapq.heappush(hq, (0, start))  # 시작노드에서 현재 노드까지 거리, 현재 노드 번호
while hq:
    dist, ci = heapq.heappop(hq)

    if distance[ci] < dist: continue  # 들어온 경로가 최단 경로가 아닌 경우

    for info in graph[ci]:
        ni, nw = info  # 다음 노드 번호와 다음 노드의 가중치
        next_dist = dist + nw
        if distance[ni] > next_dist:
            distance[ni] = next_dist
            heapq.heappush(hq, (next_dist, ni))

for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])