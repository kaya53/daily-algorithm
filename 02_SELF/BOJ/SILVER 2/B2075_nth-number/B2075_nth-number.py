# 소요시간 30분
# 우선 순위 큐를 사용한다
# - 문제에서 n번째 큰 수를 원하는 것이었으므로 => 큐에 N개 이상은 두지 않는다
# - N개가 넘어가면 hq에서 pop을 해서 작은 수는 빼내고 큰 수를 넣는다

import sys
sys.stdin = open('input.txt')

import heapq

N = int(input())
hq = []
for _ in range(N):
    for p in map(int, input().split()):
        heapq.heappush(hq, p)
        if len(hq) > N: heapq.heappop(hq)

print(heapq.heappop(hq))