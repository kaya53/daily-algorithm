# 플로이드 워셜 사용 => python 268ms
import sys
import heapq

sys.stdin = open('input.txt')


def fw():
    for k in range(N):
        for ii in range(N):
            for jj in range(N):
                #print(k+1, ii+1, jj+1)
                graph[ii][jj] = min(graph[ii][jj], graph[ii][k] + graph[k][jj])


# 노드 수, 수색 범위, 간선 수
N, M, R = map(int, input().rstrip().split())
items = list(map(int, input().rstrip().split()))

INF = int(1e9)
graph = [[INF] * N for _ in range(N)]
for _ in range(R):
    s, e, v = map(int, input().rstrip().split())
    graph[s-1][e-1] = v
    graph[e-1][s-1] = v

for i in range(N):
    graph[i][i] = 0

fw()

maxV = 0
for line in graph:
    nowV = 0
    for l in range(N):
        if line[l] <= M: nowV += items[l]
    if maxV < nowV: maxV = nowV
    # print(nowV, line)
print(maxV)



