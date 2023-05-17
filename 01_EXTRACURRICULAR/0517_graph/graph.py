import sys
sys.stdin = open("graph_input.txt")

# 무향 그래프의 인접 행렬
V = int(input())
E = int(input())
adj = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e = map(int, input().split())
    adj[s][e] = 1
    adj[e][s] = 1

for a in adj:
    print(a)


# 인접 리스트
adj_ls = [[] for _ in range(V)]
for _ in range(E):
    s, e = map(int, input().split())
    adj_ls[s].append(e)
    adj_ls[e].append(s)
for a in adj_ls:
    print(a)

# 간선 리스트
edge = [None] * E
for i in range(E):
    s, e = map(int, input().split())
    edge[i] = (s, e)
for ee in edge:
    print(ee)