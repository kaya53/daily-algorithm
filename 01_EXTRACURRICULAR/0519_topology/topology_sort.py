import sys
from collections import deque

sys.stdin = open('topologysort_input.txt')


def bfs(q):
    while q:
        now = q.popleft()
        res.append(now)

        for nnext in adj[now]:
            in_degree[nnext] -= 1
            if not in_degree[nnext]: q.append(nnext)


# for _ in range(3):
V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]
in_degree = [0] * (V+1)  # 각 정점의 진입 차수 기록
# visited = [0] * (V+1)
for _ in range(E):
    s, e = map(int, input().split())
    adj[s].append(e)
    in_degree[e] += 1

que = deque([i for i in range(1, V+1) if not in_degree[i]])

res = []
bfs(que)
# print(res, in_degree, sep='\n')
if len(res) == V:
    print(" ".join(map(str, res)))
else:
    print("cycle")