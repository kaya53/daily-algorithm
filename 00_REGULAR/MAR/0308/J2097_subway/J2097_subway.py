# BFS
# 경우의 수가 1로 시작하는 순열로 생성되어서 경우의 수가 많음 => 재귀로 풀기 어려움

# BFS 설계
# 1. 시작점과 도착점 : 1, 최대 N개 -> 시작점이 같으니까 도착점이 달라도 BFS 한번만 돌리면 모든 경로를 알 수 있음
# 2. 인접: 자기 자신이 아닌 모든 지하철역 -> 방문했던 곳 또 방문 가능
# 3. 방문 표시: 해당 지하철역까지 소요되는 가장 짧은 시간 저장; 초기값: int(1e9), math.inf와 같은 아주 큰 값
# 4. 그 외 도구: 경로 저장도 해야 함; 역 번호와 시간을 한 번에 저장
# 5. 가지 치기: curr_val >= visited[adj]인 경우; 들어온 경로가 지금 경로보다 더 길다면 가지치기
import sys

sys.stdin = open('input.txt')

import heapq

n, m = map(int, input().split())  # 지하철 역의 수, 도착역
adj = [list(map(int, input().split())) for _ in range(n)]
INF = int(1e9)
visited = [[INF, 0] for _ in range(n)]  # 출발 점에서 각 역까지 최단 시간, 경로들

q = [(0, 0)]
# q.append((0, 0))

while q:
    now, time = heapq.heappop(q)
    if time > visited[now][0]: continue
    # if now == m-1: break  # !!!도착했다고 끝이 아니라 다른 더 좋은 경로가 있을 수 있기 때문에 이 부분을 넣으면 안된다!!!
    for k in range(n):  # now에서 지하철 역까지 소요되는 시간
        if k == now : continue
        if visited[k][0] > time + adj[now][k]:
            visited[k][0] = time + adj[now][k]
            visited[k][1] = now  # 그 전 정류장
            heapq.heappush(q, (k, time + adj[now][k]))

# print(visited, m, visited[m-1][0])

print(visited[m-1][0])
res = [m]
while m != 1:
    res.append(visited[m-1][1] + 1)
    m = visited[m-1][1] + 1

print(*res[::-1])

