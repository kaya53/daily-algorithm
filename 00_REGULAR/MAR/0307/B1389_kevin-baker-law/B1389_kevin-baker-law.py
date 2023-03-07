import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs(start):
    # 현재 노드 번호, 연결된 노드 수
    global minSum
    turn_sum = 0
    for k in range(1, n+1):
        q = deque()
        q.append(start)
        visited = [0] * (n + 1)
        visited[start] = 1
        # if not visited[k]:
        while q:
            now = q.popleft()
            if now == k: break
            for nnext in adj[now]:
                if not visited[nnext]:
                    visited[nnext] = visited[now] + 1
                    q.append(nnext)
        turn_sum += visited[k]-1
    if minSum > turn_sum:
        minSum = turn_sum
    res_ls[start] = turn_sum


n, m = map(int, input().split())  # 노드의 수, 간선의 수
adj = [[] for _ in range(n+1)]
res_ls = [0] * (n+1)
for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
# 친구 관계 중복 제거
for x in range(n):
    adj[x] = list(set(adj[x]))

minSum = int(1e9)
for start in range(1, n+1):
    bfs(start)

# 제일 작은 애 뽑아내기
for idx in range(1, n+1):
    if res_ls[idx] == minSum:
        print(idx)
        break