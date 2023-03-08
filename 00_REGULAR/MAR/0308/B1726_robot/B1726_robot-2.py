## 로봇이 동서남북 방향성까지 가지기 때문에 3차원 배열을 이용해 방문을 표시해주어야 하는 문제
## 모든 좌표의 명령의 수 == 최단 경로이다.
## 즉 BFS를 활용하면 출발점에서 도착점에 다다르는 최단 경로를 한번의 연산만으로도 구할 수 있기 때문에
## 방문 표시는 방문하지 않았을 때 한번만 해줘도 이미 최단임이 보증된다.

## 경로 찾기(일사량 문제)에서는 일사량을 덜 맞는 최단 경로 + 시간까지 고려해야 했기 때문에 방문 표시를 여러번 해줘야 했다. -- 다익스트라처럼
## BUT 이 문제는 최단 경로만을 묻는 문제이기 때문에 방문 표시를 갱신할 필요가 없다.

import sys

sys.stdin = open('input.txt')

from collections import deque

r, c = map(int, input().split())  # 100이하의 자연수
arr = [list(map(int, input().split())) for _ in range(r)]
si, sj, sd = map(int, input().split())
ei, ej, ed = map(int, input().split())
si -= 1
sj -= 1
sd -= 1
ei -= 1
ej -= 1
ed -= 1

# 출발점에서 ci, cj까지 각 방향별로 최소 명령 수
orders = [[[0]*4 for _ in range(c)] for _ in range(r)]
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 동서남북 순
change = [[3, 2], [2, 3], [0, 1], [1, 0]]  # 동서남북 각각이 왼/오 90도 회전했을 때의 방향

q = deque()
q.append((si, sj, sd, 0))  # 현재 로봇의 좌표, 현재 로봇 방향, 해당 방향으로 로봇이 왔을 때 출발점으로부터 명령의 수
orders[si][sj][sd] = 0 

while q:
    ci, cj, now_dir, num = q.popleft()
    # 종료 조건
    if ci == ei and cj == ej and now_dir == ed:
        print(orders[ei][ej][ed])
        # print(q)
        break
    
    # 0. 방향 전환하기
    for next_dir in change[now_dir]:
        if not orders[ci][cj][next_dir]:
            orders[ci][cj][next_dir] = num + 1
            q.append((ci, cj, next_dir, num + 1))
    
    # 1. 해당 방향으로 이동한다 ; 1칸 ~ 3칸
    for k in range(1, 4):
        ni, nj = ci + (delta[now_dir][0]*k), cj + (delta[now_dir][1]*k)
        # 인덱스 밖, 길이 없으면 continue
        if ni < 0 or ni >= r or nj < 0 or nj >= c or arr[ni][nj] == 1: break
        if not orders[ni][nj][now_dir]:
            orders[ni][nj][now_dir] = num + 1
            q.append((ni, nj, now_dir, num + 1))
