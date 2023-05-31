# 230531 python 243ms => 2시간 ~ 2시간 30분 소요
# 문제 조건 설명이 애매하게 되어있어서 한참 봤다...
import sys

sys.stdin = open('input.txt')

from collections import deque


def move():
    global remain
    
    for now in range(N-2, -1, -1):
        if moving[now] == 0: continue  # 이동할 사람이 없음
        nnext = now + 1

        if moving[nnext] == 0 and stability[nnext] > 0:
            stability[nnext] -= 1
            if stability[nnext] == 0: remain -= 1  # 안정성이 0인 판
            if nnext == N-1:
                # print('out2')
                moving[now] = 0
            else:
                moving[nnext] = 1
                moving[now] = 0


# for _ in range(2):
N, K = map(int, input().split())
stability = deque(list(map(int, input().split())))
moving = deque([0] * (2*N))

remain = K
turn = 0
while True:
    turn += 1
    # print(turn)
    # 1. 회전
    moving.rotate()
    stability.rotate()
    if moving[N-1] == 1:
        # print('out1')
        moving[N-1] = 0
    
    # 2. 이동
    move()
    if not moving[0] and stability[0] > 0:
        moving[0] = 1
        stability[0] -= 1
        if stability[0] == 0: remain -= 1
    if moving[N - 1]:
        # print('out3')
        moving[N - 1] = 0
    # print('after ppl in ')
    # print(moving)
    # print(stability)
    # print()
    if remain <= 0:
        print(turn)
        break
