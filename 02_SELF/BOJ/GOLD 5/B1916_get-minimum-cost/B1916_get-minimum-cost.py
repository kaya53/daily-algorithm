import sys

sys.stdin = open('input.txt')

import heapq

INF = int(1e9)

def solution():
    N = int(input())
    M = int(input())
    buses = [[] for _ in range(N)]
    for _ in range(M):
        s, e, fee = map(int, input().split())
        buses[s-1].append((e-1, fee))
    # print(buses)
    start, end = map(lambda x: int(x)-1, input().split())
    q = []
    cost = [INF] * N
    heapq.heappush(q, (start, 0))
    cost[start] = 0

    while q:
        curr, curr_fee = heapq.heappop(q)
        if cost[curr] < curr_fee: continue  # 이거 넣으니까 시초 해결됨
        # 여기에 넣으면 틀리는데 while 문 빠져나와서 리턴하면 맞음
        # end를 만났다고 무조건 리턴하면 그 비용이 최소라는 보장이 없음
        # => 그래서 while문이 끝났을 때 리턴해줘야 함
        # if curr == end: return cost[end] 

        nnext = buses[curr]
        for next_stop, next_fee in nnext:
            tot = curr_fee + next_fee
            if cost[next_stop] > tot:
                cost[next_stop] = tot
                heapq.heappush(q, (next_stop, tot))
    return cost[end]


print(solution())
