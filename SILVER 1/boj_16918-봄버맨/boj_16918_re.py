import sys
from collections import deque

sys.stdin = open('input.txt')


# 폭탄 설치 함수
def set_bomb(arr):  # arr - 현재까지의 격자판 상태
    bomb_in = []
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '.' :
                arr[i][j] = 'O'
                bomb_in.append((i, j))
    bombs_stack.append(bomb_in)
    return arr


# 폭탄을 터트리는 함수
def fire_bomb(arr):  # arr - 현재까지의 격자판 상태
    di, dj = [-1, 1, 0, 0, 0], [0, 0, -1, 1, 0]
    bomb_out = bombs_stack.popleft()
    for bomb in bomb_out:
        i, j = bomb
        for k in range(5):
            ni, nj = i+di[k], j+dj[k]
            if (0 <= ni < r) and (0 <= nj < c):
                arr[ni][nj] = '.'
    return arr


for i in range(4):
    r, c, n = map(int, input().split())  # i, j, 활동 시간
    arr = [[] for _ in range(r)]
    bombs_stack = deque()

    # 초기 설정
    # arr 구성
    for i in range(r):
        tmp = input()
        for elem in tmp:
            arr[i].append(elem)

    # arr에서 폭탄 위치 찾기
    bomb_now = []
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'O':
                bomb_now.append((i, j))
    bombs_stack.append(bomb_now)
    # print(bombs_stack)

    # 2초부터 n초까지 시작; 짝수 초 -> 설치, 홀수 초 -> 폭발
    for sec in range(2, n+1):
        if not (sec % 2):
            set_bomb(arr)
        else:
            fire_bomb(arr)

    for elem in arr:
        print(*elem, sep='')
    print('-------------')