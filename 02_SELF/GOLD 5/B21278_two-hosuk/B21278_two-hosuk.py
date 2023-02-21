import sys

sys.stdin = open('input.txt')

v, e = map(int, input().split())
infos = [tuple(map(int, input().split())) for _ in range(e)]
adj = [[] for _ in range(v+1)]

# 양방향 그래프이므로
for x, y in infos:
    adj[x].append(y)
    adj[y].append(x)

# print(adj)

visited = [-1] * (v+1)
def DFS(si, ei, tot_d, tot_n):
    if si == ei:
        if tot_n < tot_d:
            tot_d = tot_n
        return tot_d
    for ni in adj[si]:
        DFS(ni, ei, tot_d, tot_n+1)


def two_chicken(combi):
    for si in range(1, v+1):
        tot_d = float('inf')  # 해당 건물에서 치킨집까지 최소 거리
        for c in combi:
            res = DFS(si, c, tot_d, 0)
            if visited[si] > -1:
                visited[si] = min(visited[si], res)
            else:
                visited[si] = res


choice = [0, 0]
candidates = []
def comb(si, cnt):
    if cnt == 2:
        candidates.append(tuple(choice))
        # 여기서 각각 choice에 대해서 최단 거리 찾기 시작
        two_chicken(choice)
        return
    for i in range(si, v+1):
        choice[cnt] = i
        comb(i+1, cnt+1)
        choice[cnt] = 0
comb(1, 0)

print(candidates)  # 건물의 조합






































