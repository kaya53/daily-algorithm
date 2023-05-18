import sys

from collections import deque

sys.stdin = open("graph_input.txt")

# 완전 탐색 코드
def bfs():
    q = deque()
    visited = [0] * V
    visited[0] = 1
    q.append(0)

    while q:
        now = q.popleft()
        for n in range(V):
            if not adj[now][n] or visited[n]: continue
            q.append(n)
            visited[n] = 1


def dfs(s):
    stack = []
    stack.append(s)
    visited = [0] * V
    visited[s] = 1

    while stack:
        now = stack.pop()
        print(now, end=' ')

        for n in range(V):
            if not adj[now][n] or visited[n]: continue
            stack.append(n)
            visited[n] = 1


# 무향 그래프의 인접 행렬
V = int(input())
E = int(input())
adj = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e = map(int, input().split())
    adj[s][e] = 1
    adj[e][s] = 1

# for a in adj:
#     print(a)
dfs(0)

# 인접 리스트
# adj_ls = [[] for _ in range(V)]
# for _ in range(E):
#     s, e = map(int, input().split())
#     adj_ls[s].append(e)
#     adj_ls[e].append(s)
# for a in adj_ls:
#     print(a)

# 간선 리스트
# edge = [None] * E
# for i in range(E):
#     s, e = map(int, input().split())
#     edge[i] = (s, e)
# for ee in edge:
#     print(ee)