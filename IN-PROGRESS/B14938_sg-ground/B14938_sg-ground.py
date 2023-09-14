import sys

sys.stdin = open('input.txt')
# input = sys.stdin.readline
from collections import deque


def bfs(start):
    q = deque([(start, M)])
    tot = items[start]
    visited[start] = 1

    while q:
        curr, left = q.popleft()

        for nnext, length in graph[curr]:
            if visited[nnext] or left-length < 0: continue
            q.append((nnext, left-length))
            visited[nnext] = 1
            tot += items[nnext]
    #         print(nnext, tot)
    # print()
    return tot


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
    visited = [0] * N
    now = bfs(i)
    if maxV < now: maxV = now

print(maxV)


