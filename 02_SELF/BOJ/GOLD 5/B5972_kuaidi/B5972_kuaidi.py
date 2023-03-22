import sys
sys.stdin = open('input.txt')

# 우선 순위 큐; 큐에 들어가는 요소 중 첫번째 요소를 기준으로 정렬이 됨
# 우선 순위 큐에 헛간 사이의 거리, 헛간 번호를 넣어준다.
# 짧은 것들(그 전에 봤던 경로가 더 짧다면 우선순위 큐에 넣어주지 않는다)만 큐에 들어가기 때문에
# 꺼내서 판별을 할 때 최단 경로만 볼 수 있다.
# 1 - n까지의 최단 경로
import heapq

n, m = map(int, input().split())
graph = [[] for i in range(n)]  # 연결 정보
for i in range(m):
    ai, bi, ci = map(int, input().split())  # 헛간1, 헛간2, 소들
    ai -= 1
    bi -= 1
    graph[ai].append((bi, ci))
    graph[bi].append((ai, ci))

INF = int(1e9)
cows_ls = [INF] * n  # 각 노드까지 최소 거리를 담은 배열

hq = []
heapq.heappush(hq, (0, 0))  # (거리, 노드)의 형태로 넣어주어야 거리가 최소인 것 순으로 pop된다
cows_ls[0] = 0
# print(graph)
while hq:
    cow, now = heapq.heappop(hq)  # 현재까지 저장된 now 노드까지 최소 소의 마리수
    # 저장되어 있는 게 이미 지금 들어온 소보다 더 적으면
    if cows_ls[now] < cow: continue
    # print(graph[now])
    for i in graph[now]:
        # print(i)
        next_cow = cow + i[1]  # 다음 경로까지 소의 마리수
        # 이번 턴에서 다음 경로까지 소의 마리수가 이전 턴에 기록된 것보다 작으면
        if next_cow < cows_ls[i[0]]:
            cows_ls[i[0]] = next_cow
            heapq.heappush(hq, (next_cow, i[0]))  # 소의 마리수, 노드 번호

print(cows_ls[-1])