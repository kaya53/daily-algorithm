# 소요시간 30분 pypy 2896ms
# - graph를 연결된 부분만 append하게 받으니까 1차 통과
# => python으로 시초 나니까 다른 방법을 생각해보자
# - 크루스칼로 다시 시도해보기
import sys

sys.stdin = open('input.txt')

from collections import deque


def get_usado():
    usado = [[0]*N for _ in range(N)]
    for s in range(N):
        usado[s][s] = -1
        que = deque([(s, int(1e9))])
        while que:
            now, mmin = que.popleft()
            for ni, nv in graph[now]:
                if usado[s][ni]: continue  # 연결 안됨
                cost = min(mmin, nv)
                # if (s, ni) == (2, 3): print('c', cost)
                usado[s][ni] = cost
                # usado[ni][s] = cost
                que.append((ni, cost))
    return usado


N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p-1].append((q-1, r))
    graph[q-1].append((p-1, r))

board = get_usado()
for b in board:
    print(b)
for _ in range(Q):
    cnt = 0
    k, v = map(int, input().split())
    for val in board[v-1]:
        if val >= k: cnt += 1
    print(cnt)
